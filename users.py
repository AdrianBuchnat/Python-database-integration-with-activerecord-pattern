import argparse
from models import User
from psycopg2.errors import UniqueViolation


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-n", "--new_password", help="new password (min 8 characters)")
parser.add_argument("-l", "--list", help="display list of users", action="store_true")
parser.add_argument("-d", "--delate", help="delate user", action="store_true")
parser.add_argument("-e", "--edit", help="edit user", action="store_true")

args = parser.parse_args()

def create_user(cursor, username, password):
    if len(password) < 8:
        print("Password is too short. It should have minimum 8 characters")
    else:
        try:
            user = User(username, password)
            user.save_to_database(cursor)
        except UniqueViolation:
            print("User alredy exist. ", UniqueViolation)

def list_users(cursor):
    users = User.load_all_users(cursor)
    for user in users:
        print(user.username)

def delete_user(cursor, username, password):
    user = User.load_by_
