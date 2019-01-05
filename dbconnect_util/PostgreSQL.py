"""
memo:

"""
import psycopg2
from dbconnect_util.DBConnectBase import DBConnectBase

class PostgreSQL(DBConnectBase):

    def connect(self, username, password, hostname, database):
        dsn = "postgresql://{}:{}@{}:{}/{}".format(
            username,
            password,
            hostname,
            5432,
            database
        )
        conn = psycopg2.connect(dsn)
        return conn

    def select(self, conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * from test_table')
        for row in cursor:
            print(row)