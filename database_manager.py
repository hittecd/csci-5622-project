import mysql.connector


HOST = "127.0.0.1"
USERNAME = "root"
PASSWORD = "password"
DATABASE = "zillow"


class DatabaseManager:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(user=USERNAME, password=PASSWORD, host=HOST, database=DATABASE)
