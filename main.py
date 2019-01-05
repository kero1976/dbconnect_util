from dbconnect_util import DBManager
from dbconnect_util import View

print("START")
db = DBManager.DBManager("MySQL")
db.connect("kero", "k0bayasi", "localhost", "testdb")


list = db.connection_list()

#db.delete_tables(list)
print("=========================")


print('END')
