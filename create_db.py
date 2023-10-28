"""
This script is used to create a database and the necessary tables for the Simple_Communicator chat application.

To use this script, it is recommended to change the following variables to match your own server settings:
- USER: Your PostgreSQL username.
- HOST: The host where your PostgreSQL server is running.
- PASSWORD: Your PostgreSQL password.

Please note that changing the names of the 'users' and 'messages' tables is possible, but not recommended, as these names are assumed by the Simple_Communicator application.

Usage:
1. Configure the USER, HOST, and PASSWORD variables.
2. Call the 'create_database' function to create the main database.
3. Call the 'create_table_users' function to create the 'users' table.
4. Call the 'create_table_messages' function to create the 'messages' table.

For questions or assistance, please refer to the Simple_Communicator documentation.
"""

from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

def create_database(database_name):
    """
    Creates a database on a PostgreSQL server.

    Args:
        database_name (str): The name of the new database.

    Raises:
        OperationalError: If there is an operational error while creating the database.
        DuplicateDatabase: If a database with the specified name already exists.

    Returns:
        None
    """
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        query = f"CREATE DATABASE {database_name}"
        cursor.execute(query)
        print(f"Database {database_name} created successfully")

    except OperationalError as err:
        print(f"Creation unsuccessfully: {err}")
    except DuplicateDatabase:
        print(f"Database {database_name} already exists")

    finally:
        cursor.close()
        cnx.close()

def create_table_users(table_name):
    """
    Creates a user table in the specified PostgreSQL database.

    Args:
        table_name (str): The name of the new user table.

    Raises:
        OperationalError: If there is an operational error while creating the table.
        DuplicateTable: If a table with the specified name already exists.

    Returns:
        None

    The table contains the following columns:
    - id (serial): The primary key for the table.
    - username (varchar(255)): The username of the user.
    - hashed_password (varchar(80)): The hashed password of the user.
    """
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        query = f"""
        CREATE TABLE {table_name}(
        id serial PRIMARY KEY, 
        username varchar(255) NOT NULL,
        hashed_password  varchar(80) NOT NULL
        );"""
        cursor.execute(query)
        print(f"Table {table_name} created successfully")

    except OperationalError as err:
        print(f"Creation unsuccessfully: {err}")
    except DuplicateTable:
        print(f"Database {table_name} already exists")

    finally:
        cursor.close()
        cnx.close()

def create_table_messages(table_name):
    """
    Creates a messages table in the specified PostgreSQL database.

    Args:
        table_name (str): The name of the new messages table.

    Raises:
        OperationalError: If there is an operational error while creating the table.
        DuplicateTable: If a table with the specified name already exists.

    Returns:
        None

    The table contains the following columns:
    - id (serial): The primary key for the table.
    - from_id (int): A reference to the user who sent the message.
    - to_id (int): A reference to the user who received the message.
    - creation_date (timestamp): Automatically generated timestamp at the time of message creation.
    - text (varchar(255)): The text of the message.
    """
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST)
        cnx.autocommit = True
        cursor = cnx.cursor()
        query = f"""
        CREATE TABLE {table_name}(
        id serial PRIMARY KEY, 
        from_id int NOT NULL REFERENCES users(id),
        to_id int NOT NULL REFERENCES users(id),
        creation_date timestamp DEFAULT current_timestamp,
        text varchar(255)
        );"""
        cursor.execute(query)
        print(f"Table {table_name} created successfully")

    except OperationalError as err:
        print(f"Creation unsuccessfully: {err}")
    except DuplicateTable:
        print(f"Database {table_name} already exists")

    finally:
        cursor.close()
        cnx.close()

create_database("testowa")
create_table_users("users")
create_table_messages("messages")


