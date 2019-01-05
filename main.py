from dbconnect_util import DBManager

print("START")
db = DBManager.DBManager("MySQL")
db.connect("kero", "k0bayasi", "localhost", "testdb")


db.table_list()
print('END')
