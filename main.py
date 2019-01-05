from dbconnect_util import DBManager

print("TEST3")
db = DBManager.DBManager("PostgreSQL")
db.connect("kero", "k0bayasi", "localhost", "testdb")
#conn = db.connect("testuser", "testpassword", "localhost", "testdb")
db.select()
print('END')
