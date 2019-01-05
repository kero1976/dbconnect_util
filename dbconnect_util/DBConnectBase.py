class DBConnectBase(object):
    def __init__(self):
        print('db init')

    def connect(self, user, password, host, dbname):
        """
        継承しtクラスでDBのコネクションを作成し、self._conに格納する
        :param user:
        :param password:
        :param host:
        :param dbname:
        :return:
        """
        pass

    def select(self, sql, output=True):
        print(sql)
        cursor = self._con.cursor()
        cursor.execute(sql)
        list = []
        for row in cursor:
            if output:
                print(row)
            list.append(row)
        cursor.close()
        return list

    def insert(self):
        cursor = self._con.cursor()
        for i in range(1000):
            cursor.execute("insert into test2 values ({}, 'A')".format(i))
        self._con.commit()
        cursor.close()

    def delete_tables(self, tables):
        cursor = self._con.cursor()
        for table in tables:
            cursor.execute("delete from {}".format(table))
        self._con.commit()
        cursor.close()

    def table_list(self, output=True):
        result = []
        # リストの要素がタプルになっているので、タプルを外して返す
        for tmp in self.select(self.table_list_sql(), output):
            result.append(tmp[0])
        return result

    def table_count(self, tables, output=True):
        result = []
        for table in tables:
            result.append(
                self.select("select '{0}', count(*) from {0}".format(table), output)[0])
        return result

    def connection_list(self, output=True):
        return self.select(self.connection_list_sql(), output)

    def show_table_column(self, table, output=True):
        return self.select(self.show_table_column_sql(table), output)
