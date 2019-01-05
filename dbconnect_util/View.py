from datetime import datetime

def table_count_view(tables_count_list):
    """
    テーブル件数を整形して出力
    :param tables_count_list:
        0列目：テーブル名
        1列目：データ件数
    :return: なし
    """
    # 件数の降順でソート
    tables_count_list.sort(key=lambda x: x[1], reverse=True)

    STYLE_SEPARATE = "{0}|{1}".format("-"*20, "-"*10)
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print(STYLE_SEPARATE)
    print("{0:^20}|{1:^10}".format("TABLE_NAME","COUNT"))
    print(STYLE_SEPARATE)
    for table in tables_count_list:
        # テーブル名を大文字にして左詰め20桁
        # データ件数は右詰め10桁でカンマで桁区切り
        print("{0:<20}|{1:>10,}".format(table[0].upper(), table[1]))
    print(STYLE_SEPARATE)
