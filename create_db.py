import psycopg2
from psycopg2 import sql

database_params = {
    'host': '127.0.0.1',
    'user': 'postgres',
    'password': 'admin12345',
}

try:
    # connection to the postgresSQL database
    connection = psycopg2.connect(**database_params)

    #Cursor object to execute SQL queries
    cursor = connection.cursor()

    #check if database alredy exist
    cursor.execute(
        sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s;"), ["databaseForProject"]
    )

    if not cursor.fetchone():
        # If database do not exist create it
        cursor.execute(
            sql.SQL("CREATE DATABASE databaseForProject;")
            )

        print("Database created successfully")

    else:
        print("Database alredy exist")

except (Exception, psycopg2.Error) as error:
    print("Error connecting to PostgresSQL database: ", error)

finally:
    # Close the database connection and cursor;
    if connection:
        cursor.close()
        connection.close()
        print("PostgresSQL connection is closed.")
