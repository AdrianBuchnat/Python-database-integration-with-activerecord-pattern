from models import User, Message
from psycopg2 import OperationalError, connect

DB_USER = "postgres"
DB_PASSWORD = "admin12345"
DB_HOST = "127.0.0.1"
DATABASE = "databaseintegration"

try:
    cnx = connect(database=DATABASE, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
except OperationalError:
    print("Connection faild")

UserTest = User("Adria121n","haslosilne113131323")
UserTest.save_to_database(cursor)

cursor.close()
cnx.close()
