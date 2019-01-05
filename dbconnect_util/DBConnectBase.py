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
        cursor = self._con.cursor()
        cursor.execute(sql)
        list = []
        for row in cursor:
            if output:
                print(row)
            list.append(row)
        cursor.close()
        return list

    def table_list(self, output=True):
        tmplist = self.select(self.table_list_sql(), output)
        result = []
        # リストの要素がタプルになっているので、タプルを外して返す
        for tmp in tmplist:
            result.append(tmp[0])
        return result

    def table_count(self, tables, output=True):
        result = []
        for table in tables:
            result.append(
                self.select("select '{0}', count(*) from {0}".format(table), output)[0])
        return result