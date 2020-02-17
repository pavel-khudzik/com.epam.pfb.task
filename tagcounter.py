import dbapi as db

"""
Main file for running the programm
    tagcounter                      -> run GUI versiom
    tagcounter --<command> options  -> run console version
   
"""

print(*db.tables_list())
#my_db.drop_table("tagcounter")

row = ('yandex', 'yandex.ru', '2020-02-17', 100)
#db.add_record(row)

print(*db.select_table())