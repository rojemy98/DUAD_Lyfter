import psycopg2
from psycopg2.extras import execute_values

class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.connection = self.create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()
            print("Connection created succesfully")

    def create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:", error)
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")

    def execute_query(self, query, *args):
        if args:
            self.cursor.execute(query, args)
        else:
            self.cursor.execute(query)

        if self.cursor.description:
            return self.cursor.fetchall()
    
    def execute_many(self, query, values):
        execute_values(
            self.cursor,
            query,
            values
        )

    def begin_transaction(self):
        self.connection.autocommit = False

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
