import argparse
from psycopg2 import connect, OperationalError
from clcrypto import check_password
from models import Message, User


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-l", "--list", help="list all messages", action="store_true")
parser.add_argument("-t", "--to", help="to")
parser.add_argument("-s", "--send", help="text message to send")

args = parser.parse_args()

def print_user_messages(cursor, user):
    """Print all massages from user
    """
    messages = Message.load_all_messages(cursor, user._id)
    if len(messages) == 0:
        print (20 * "#")
        print ("User has no masseges")
        print (20 * "#")
    else:
        for message in messages:
            from_ = User.load_user_by_id(cursor, message.from_id)
            print( 20 * "#")
            print(f"from: {from_.username}")
            print(f"data: {message._creation_date}")
            print('"', message.text, '"')
            print( 20 * "#")

def send_message(cursor, from_id, recipient_name, text):
    """Send massage to user:
        cursor -> object form psycopg2 to interact with database
        from_id -> who sending message
        recipient_name -> to who we send messege
        test -> content of the massage that we send
        """
    if len(text) > 255:
        print("Message is too long!")
        return
    to = User.load_user_by_username(cursor, recipient_name)
    if to:
        message = Message(from_id, to._id, text=text)
        message.save_to_database(cursor)
        print("Message send")
    else:
        print("Recipient does not exists.")


if __name__ == '__main__':
    DB_USER = "postgres"
    DB_PASSWORD = "admin12345"
    DB_HOST = "127.0.0.1"
    DATABASE = "databaseintegration"

    try:
        cnx = connect(database=DATABASE, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        if args.username and args.password:
            user = User.load_user_by_username(cursor, args.username)
            if check_password(args.password, user.hashed_password):
                if args.list:
                    print_user_messages(cursor, user)
                elif args.to and args.send:
                    send_message(cursor, user.id, args.to, args.send)
                else:
                    parser.print_help()
            else:
                print("Incorrect password or User does not exists!")
        else:
            print("username and password are required")
            parser.print_help()
        cnx.close()
    except OperationalError as err:
        print("Connection Error: ", err)
