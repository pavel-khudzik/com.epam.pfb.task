import dbapi as db
from logsite import log_site
from synomyms import get_site_by_synonym


"""
Main file for running the programm
    tagcounter                      -> run GUI versiom
    tagcounter --<command> options  -> run console version
"""

"""
    work with DB
"""
#print(*db.tables_list())
#my_db.drop_table("tagcounter")
#db.add_record(('yandex', 'yandex.ru', '2020-02-17', {html: 10 ...}))
#print(*db.select_table())

"""
    sites logging
"""
#log_site('news.tut.by')

"""
    work with yaml list
"""
#print(get_site_by_synonym('ydx'))

