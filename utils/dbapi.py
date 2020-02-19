import sqlite3

"""
DB table description
    - имя сайта (домен второго уровня)
    - url
    - дата проверки
    - данные о тэгах
"""

DB_PATH = 'tagcounter.db'
TABLE_NAME = 't_tagcounter'


#
def create_table(tab_name=None):
    conn = sqlite3.connect(DB_PATH)

    if not tab_name:
        tab_name = TABLE_NAME

    cur = conn.cursor()

    cur.execute('SELECT COUNT(1) FROM sqlite_master WHERE type="table" AND name=?', (tab_name,))
    if cur.fetchone()[0] == 0:
        cur.execute('CREATE TABLE ' + tab_name + '(site TEXT, url TEXT, date_of_check TEXT, tag_info TEXT)')

    conn.close()


#
def drop_table(tab_name=None):
    conn = sqlite3.connect(DB_PATH)

    if not tab_name:
        tab_name = TABLE_NAME

    cur = conn.cursor()
    cur.execute('DROP TABLE ' + tab_name)

    conn.close()


#
def add_record(new_row, tab_name=None):
    conn = sqlite3.connect(DB_PATH)

    if not tab_name:
        tab_name = TABLE_NAME

    create_table(tab_name)

    cur = conn.cursor()

    cur.execute('INSERT INTO ' + tab_name + ' VALUES(?,?,?,?)', new_row)

    conn.commit()
    conn.close()


#
def tables_list():
    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()
    cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
    tabs_list = cur.fetchall()

    conn.close()

    for tab in tabs_list:
        print(tab[0])


#
def select_table(site_url=None, tab_name=None):
    conn = sqlite3.connect(DB_PATH)

    if not tab_name:
        tab_name = TABLE_NAME

    cur = conn.cursor()
    if site_url:
        cur.execute('SELECT * FROM ' + tab_name + ' WHERE url=? ORDER BY date_of_check DESC', (site_url, ))
    else:
        cur.execute('SELECT * FROM ' + tab_name)

    rows_list = cur.fetchall()

    conn.close()

    return rows_list

#
def clear_table(tab_name=None):
    conn = sqlite3.connect(DB_PATH)

    if not tab_name:
        tab_name = TABLE_NAME

    cur = conn.cursor()
    cur.execute('DELETE FROM ' + tab_name)
    conn.commit()

    conn.close()

