import argparse
from models import User
from psycopg2.errors import UniqueViolation
from clcrypto import check_password
from psycopg2 import OperationalError, connect


# Creating a parser object and add possible operation to it.
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-n", "--new_password", help="new password (min 8 characters)")
parser.add_argument("-l", "--list", help="display list of users", action="store_true")
parser.add_argument("-d", "--delate", help="delate user", action="store_true")
parser.add_argument("-e", "--edit", help="edit user", action="store_true")

args = parser.parse_args()

def create_user(cursor, username, password):
    """Create new user:
            cursor -> object from psycopg2 to operate at databases
            username -> String username
            password -> String password with minimum 8 characters
    """
    if len(password) < 8:
        print("Password is too short. It should have minimum 8 characters")
    else:
        try:
            user = User(username, password)
            user.save_to_database(cursor)
        except UniqueViolation:
            print("User alredy exist. ", UniqueViolation)

def list_users(cursor):
    """Display users from database:
        cursor -> object form psycopg2 to operate at database"""
    users = User.load_all_users(cursor)
    for user in users:
        print(user.username)

def delete_user(cursor, username, password):
    """
    delate user form database:
        cursor -> object from psycopg2 to operate at databases
        username -> String username
        password -> String user password
    """
    user = User.load_user_by_username(cursor, username)
    if not user:
        print("User does not exist")
    elif check_password(password, user._hashed_password):
        user.delete(cursor)
    else:
        print("Incorrect password")

def edit_user(cursor, username, old_password, new_password):
    """
    edit user in database:
        cursor -> object from psycopg2 to operate at databases
        username -> String username
        old_password -> String user password
        new_password -> String with at least 8 characters whos will be new user password.
    """
    user = User.load_user_by_username(cursor, username)
    if not user:
        print("User does not exist")
    elif check_password(old_password, user._hashed_password):
        if len(new_password) < 8:
            print("New password is to short, it should have minimum 8 characters")
        else:
            user.set_password(new_password)
            user.save_to_database(cursor)
            print("Password changed")
    else:
        print("Incorrect password")


if __name__ == "__main__":
    DB_USER = "postgres"
    DB_PASSWORD = "admin12345"
    DB_HOST = "127.0.0.1"
    DATABASE = "databaseintegration"

    try:
        cnx = connect(database=DATABASE, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()

        if args.username and args.password and args.edit and args.new_password:
            edit_user(cursor, args.username, args.password, args.new_password)
        elif args.username and args.password and args.delate:
            delete_user(cursor, args.username, args.password)
        elif args.username and args.password:
            create_user(cursor, args.username, args.password)
        elif args.list:
            list_users(cursor)
        else:
            parser.print_help()

    except OperationalError:
        print("Connection faild: ", OperationalError)
