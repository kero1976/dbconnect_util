"""
memo:
    mysql-connector-pythonだとWindows環境のMySQL8だと接続時にエラーが出た
"""
import mysql.connector
from dbconnect_util.DBConnectBase import DBConnectBase

class MySQL(DBConnectBase):

    def connect(self, username, password, host, db):
        conn = mysql.connector.connect(
            host = host,
            user = username,
            passwd = password,
            db = db)
        self._con = conn

    def table_list_sql(self):
        return "show tables"