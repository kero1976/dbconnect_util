from dbconnect_util import DBManager
from dbconnect_util import View

print("START")
db = DBManager.DBManager("MySQL")
db.connect("kero", "k0bayasi", "localhost", "testdb")

db.insert()

list = db.table_list(False)
#db.delete_tables(list)
print("=========================")
list2 = db.table_count(list, False)
View.table_count_view(list2)

print('END')
