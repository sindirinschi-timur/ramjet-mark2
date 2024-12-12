import mysql.connector
from flask import current_app

def get_db_connection():
    config = current_app.config['DB_CONFIG']
    config['charset'] = 'utf8mb4'
    return mysql.connector.connect(**config)


def query_db(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or ())
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def execute_db(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    conn.commit()
    cursor.close()
    conn.close()
