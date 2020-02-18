import logging

"""
Логирование прочитаных сайтов, ведется в специальный файл.
Формат файла: дата время название_сайта
"""

logging.basicConfig(filename='tagcounter.log', level=logging.INFO, format='%(asctime)-20s %(message)s')


def log_site(site_name):
    logging.info(site_name)

