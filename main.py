from dbconnect_util import DBConnectBase
from dbconnect_util import MySQL

print("TEST2")
db = MySQL.MySQL()
conn = db.connect("kero", "k0bayasi", "localhost", "test_mysql_database")
db.select(conn)
print('END')
