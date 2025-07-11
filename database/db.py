import mysql.connector
from config import Config


def get_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        return connection
    except Exception as e:
        print("Error: Can't connect to database", e)
        return None;

