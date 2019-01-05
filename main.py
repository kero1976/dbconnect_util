from dbconnect_util import DBConnectBase
from dbconnect_util import MySQL
from dbconnect_util import PostgreSQL
print("TEST3")
db = PostgreSQL.PostgreSQL()
#conn = db.connect("kero", "k0bayasi", "localhost", "test_mysql_database")
conn = db.connect("testuser", "testpassword", "localhost", "testdb")
db.select(conn)
print('END')
