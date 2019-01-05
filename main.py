from dbconnect_util import DBManager

print("START")
db = DBManager.DBManager("PostgreSQL")
db.connect("kero", "k0bayasi", "localhost", "testdb")


list = db.table_list()
print("=========================")
list2 = db.table_count(list, False)
list2.sort(key=lambda x:x[1], reverse=True)
for table in list2:
    print("{},{}".format(table[0], table[1]))

print('END')
