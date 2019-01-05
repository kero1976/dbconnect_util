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
        self._con = conn

    def table_list(self):
        self.select("select relname as TABLE_NAME from pg_stat_user_tables")