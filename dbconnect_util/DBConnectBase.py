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

    def select(self, sql):
        cursor = self._con.cursor()
        cursor.execute(sql)
        for row in cursor:
            print(row)
