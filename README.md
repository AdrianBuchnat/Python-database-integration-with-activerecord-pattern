
# Console Messaging App

This is a console application for sending messages. It can be controlled through the console using the argparse module. The application connects to a PostgreSQL database using the psycopg2 tool (included in the requirements.txt file). This is a demonstration project, so there won't be any possibility to commit to it. It is intended for use in my CV/portfolio. To run the project locally, you need to have Python installed. The file for creating a new database is named "create_db.py" in the project. Just replace the username and password that allow you to log in to PostgreSQL.

### Techstack
![python](https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png=250x) ![PostgreSQL](https://user-images.githubusercontent.com/25181517/117208740-bfb78400-adf5-11eb-97bb-09072b6bedfc.png=250x)
## Installation

Make sure you have Python installed. Run the following command to install the required dependencies:

```bash

pip install -r requirements.txt
```
Run the database creation script:

```bash

python create_db.py
```
## Usage
Managing Users

Commands for managing users are executed using the python users command.

```bash

python users.py -u <username> -p <password>
```
To list all users:

```bash

python users.py --list / -l
```
To edit a user's password, provide the username, current password, and the new password:

```bash

python users -u <username> -p <current_password> -n <new_password> --edit
```
To delete a user, provide the username and password:

```bash
python users -u <username> -p <password> --delete
```
## Managing Messages

You can also manage messages through the messages file.

To send a message, provide the sender's username, password, recipient's username, and the message content:

```bash

python messages.py -u <sender_username> -p <sender_password> -t <recipient_username> -s <message_content>
```
To display all received messages, provide the username and password:

```bash

python messages -u <username> -p <password> --list
```
Feel free to explore and use this console messaging app for your personal projects.
