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

# Adding user to database. 
# UserTest = User("Adria121n","haslosilne113131323")
# UserTest.save_to_database(cursor)

# load user from database
# UserTest = User.load_user_by_id(cursor, 1)
# print(f"{UserTest}: Username: {UserTest.username}, password: {UserTest.hashed_password}, id: {UserTest.id}")

# check if invalid id number returns None
# UserTestNone = User.load_user_by_id(cursor, 300)
# print(UserTestNone)
    
# load users
# Users = User.load_all_users(cursor)
# print(User)
# for user in Users:
#     print(f"Username: {user.username}, password: {user.hashed_password}, id: {user.id}")

# Test for update user
# user_test = User.load_user_by_id(cursor, 2)
# user_test.username = "UpdatedAdrian"
# user_test.save_to_database(cursor)

# Test for delate user from database
# Create user to Delate
# user_test = User("AdriaToDelate","hasloTestDelete")
# user_test.save_to_database(cursor)
# print(user_test._id)
#Delate that user
# user_to_delate = User.load_user_by_id(cursor, 4)
# print(user_to_delate._id)
# user_to_delate.delete(cursor)

# Messages tests:
# test_message = Message(1, 2, "Hello Adrian, i am fine, thanks for asking")
# test_message.save_to_database(cursor)

# Load all massages
# messages = Message.load_all_messages(cursor)
# for message in messages:
#     print(f"From: {message.from_id}, to: {message.to_id}, text: {message.text}")



cursor.close()
cnx.close()
