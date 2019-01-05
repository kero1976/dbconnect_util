"""
memo:

"""
import psycopg2
from dbconnect_util.DBConnectBase import DBConnectBase

class PostgreSQL(DBConnectBase):

    def connect(self, username, password, hostname, database):
        dsn = "postgresql://{}:{}@{}:{}/{}".format(
            username,
            password,
            hostname,
            5432,
            database
        )
        conn = psycopg2.connect(dsn)
        self._con = conn

    def table_list_sql(self):
        return "select relname as TABLE_NAME from pg_stat_user_tables"

    def connection_list_sql(self):
        return """\
        select \
pid ,\
to_char(backend_start,'YYYY/MM/DD HH24:MI:SS'),\
usename ,\
application_name ,\
client_addr ,\
client_port ,\
state ,\
query \
from pg_stat_activity"""

    def show_table_column_sql(self, table):
        sql = """ \
select \
 * \
from \
 information_schema.columns \
where \
 table_name = '{}' \
order by ordinal_position """.format(table)
        return sql