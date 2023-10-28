from psycopg2 import connect, OperationalError

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
database_name = "simple_communicator"

cnx = connect(user=USER, password=PASSWORD, host=HOST, database = database_name)
cnx.autocommit = True
cursor = cnx.cursor()