import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="1Whitetiger$",
        database="TaskManagerDB"
    )


