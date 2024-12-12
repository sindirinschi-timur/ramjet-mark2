from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    app.config['DB_CONFIG'] = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': 'localhost',
        'port': os.getenv('DB_PORT'),
        'database': 'ramjet_db',
        'autocommit':True,
        'charset':"utf8mb4",
        'collation':"utf8mb4_general_ci"
    }

    from routes import main_routes
    app.register_blueprint(main_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
