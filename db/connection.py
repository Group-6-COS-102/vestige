import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="vestige_db",
        user="postgres",
        password="cos101",
        port="5432"
    )

    return connection
