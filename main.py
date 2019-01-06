from dbconnect_util import DBManager
from dbconnect_util import View

print("START")
db = DBManager.DBManager("PostgreSQL")
db.connect("kero", "k0bayasi", "localhost", "testdb")

db.copy_table("test2")

View.table_count_view(db.table_count(db.table_list(False)))


print("=========================")


print('END')
