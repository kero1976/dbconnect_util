from dbconnect_util import DBConnectBase
from dbconnect_util import MySQL
from dbconnect_util import PostgreSQL

class DBManager(object):
    """
    使い方:
        1.引数に"MySQL" or "PostgreSQL"を渡してインスタンスを作成する
            dbm = DBManager("MySQL")
        2.ユーザ名、パスワード、ホスト名、DB名を渡してコネクションを張る
            dbm.connect("user", "pass", "localhost", "test_db")
        3-1.テーブルの一覧取得
            table_list = dbm.table_list()
        3-2.テーブルの件数取得
            table_count_list = dbm.table_count(table_list)
        3-3.テーブルのデータ削除(全件)
            dbm.delete_tables(table_list)
        3-4.テーブルのコピー作成
            db.copy_table(table)

    """
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

    def insert(self):
        self._db.insert()

    def delete_tables(self, tables):
        self._db.delete_tables(tables)

    def connection_list(self, output=True):
        return self._db.connection_list(output)

    def show_table_column(self, table, output=True):
        return self._db.show_table_column(table, output)

    def copy_table(self, tables):
        self._db.copy_table(tables)