import sqlite3

"""
Main file for running the programm
    tagcounter                      -> run GUI versiom
    tagcounter --<command> options  -> run console version
    
DB
    - имя сайта (домен второго уровня)
    - url
    - дата проверки
    - данные о тэгах

"""

conn = sqlite3.connect('tagcounter.db')
c = conn.cursor()
c.execute('''CREATE TABLE tagcounter
             (site text, url text, data_of_check text, tag_info real, price real)''')

