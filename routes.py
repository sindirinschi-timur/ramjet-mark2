from flask import Blueprint, render_template, request, redirect, url_for, session
from db_utils import query_db, execute_db
from geopy.distance import geodesic

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/start_game', methods=['POST'])
def start_game():
    player_name = request.form['player_name']
    session['player_name'] = player_name
    execute_db("INSERT INTO game (player_name) VALUES (%s)", (player_name,))
    return redirect(url_for('main.choose_species'))

@main_routes.route('/choose_species', methods=['GET', 'POST'])
def choose_species():
    if request.method == 'POST':
        species = request.form['species']
        session['species'] = species  

        species_mapping = {'Shadow': 1, 'Suede': 2}  
        species_id = species_mapping[species]
        
        execute_db("UPDATE game SET species = %s WHERE player_name = %s", (species_id, session['player_name']))
        return redirect(url_for('main.assign_frigates'))
    return render_template('choose_species.html')


@main_routes.route('/assign_frigates')
def assign_frigates():
    species = session['species']

    frigates = query_db("SELECT name FROM frigates WHERE name = %s AND price = 0", (species,))
    session['frigates'] = [frigate['name'] for frigate in frigates]
    return redirect(url_for('main.quest'))

@main_routes.route('/quest', methods=['GET', 'POST'])
def quest():
    player = query_db("SELECT * FROM game WHERE player_name = %s", (session['player_name'],))

    if not player:
        return "Player not found.", 404

    player = player[0]
    current_quest_id = player['current_quest_id']

    quest = query_db("SELECT * FROM quests WHERE id = %s", (current_quest_id,))

    if not quest:
        return render_template('the_end.html')

    quest = quest[0]

    npc = query_db("SELECT * FROM npcs WHERE id = %s", (quest['id'],))
    npc = npc[0] if npc else None

    if request.method == 'POST':
        input_code = request.form['iata_code']

        if input_code == quest['iata_code']:
            airport = query_db("SELECT * FROM airports WHERE ident = %s", (input_code,))

            if not airport:
                return "Invalid airport code.", 400

            airport = airport[0]
            current_location = (airport['latitude_deg'], airport['longitude_deg'])
            destination = (airport['latitude_deg'], airport['longitude_deg'])
            distance = geodesic(current_location, destination).km * 0.1
            reward = 100 + int(distance)
            balance = reward + player['concords']
            execute_db(
                "UPDATE game SET concords = concords + %s, current_quest_id = current_quest_id + 1 WHERE player_name = %s",
                (balance, player['player_name'])
            )

            return render_template('reward.html', reward=reward, npc_name=npc['name'], dialogue = npc['dialogue'])

    return render_template('quest.html', quest=quest, npc=npc)



