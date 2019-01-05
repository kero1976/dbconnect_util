from dbconnect_util import DBConnectBase
from dbconnect_util import MySQL
from dbconnect_util import PostgreSQL

class DBManager(object):
    def __init__(self, db_type):
        if db_type == "MySQL":
            self._db = MySQL.MySQL()
        elif db_type == "PostgreSQL":
            self._db = PostgreSQL.PostgreSQL()
        else:
            raise TypeError("MySQLとPostgreSQL以外は対応していません")

    def connect(self, user, password, host, dbname):
        self._con = self._db.connect( user, password, host, dbname)

    def select(self, sql):
        self._db.select(sql)

    def table_list(self, output=True):
        return self._db.table_list(output)

    def table_count(self, tables, output=True):
        return self._db.table_count(tables, output)