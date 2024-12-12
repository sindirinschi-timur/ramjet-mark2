from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(255), nullable=False)
    species = db.Column(db.String(255), nullable=False)

class Frigate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    species = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    iata_code = db.Column(db.String(10), nullable=False)
    npc_id = db.Column(db.Integer, nullable=False)

class NPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    dialogue = db.Column(db.Text, nullable=False)

class Airport(db.Model):
    id = db.Column(db.Integer(11), primary_key=True)
    ident = db.Column(db.String(40), nullable=False)
    type = db.Column(db.String(40), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    latitude_deg = db.Column(db.Double, nullable=False)
    longitude_deg = db.Column(db.Double, nullable=False)
    iata_code = db.Column(db.String(40), nullable=False)
    iso_country = db.Column(db.String(40), foreign_key=True, nullable=False)
    municipality = db.Column(db.String(40), nullable=False)

class Country(db.Model):
    iso_country = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    continent = db.Column(db.String(40), nullable=False)