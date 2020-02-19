from html.parser import HTMLParser
import requests
import yaml
import logging
import pickle
from datetime import datetime

import utils.dbapi as db


# Class for counting tags
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_dict = {}

    def handle_starttag(self, tag, attrs):
        self.tag_dict[tag] = self.tag_dict.setdefault(tag, 0) + 1


# Function return content of the site
def get_site_content(site_url):
    ret = ''

    try:
        ret = requests.get(site_url).text
    except:
        ret = ''

    return ret


# Function count amount of tags and return dictionary: {<tag_name>: <count>}
def get_tag_count(site_url):
    parser = MyHTMLParser()

    parser.feed(get_site_content(site_url))

    return parser.tag_dict


"""
    Для удобства работы, создать файл с синонимами в формате yaml. 
    Данный файл для каждого сайта опредляет синоним, например: ydx: yandex.ru ggl: google.com
    
    Для примера, к программе приложить файл с несколькими синонимами. 
    Пользователи сами дложны иметь возможность добавлять, удалять данные из файла.
"""


def get_site_by_synonym(synonym):
    synonyms_dct = {}

    try:
        synonyms_dct = yaml.safe_load(open('tagcounter.yaml'))
    except FileNotFoundError:
        with open('tagcounter.yaml', 'a') as yf:
            pass

    if synonyms_dct:
        return synonyms_dct.setdefault(synonym, synonym)
    else:
        return synonym


"""
    Логирование прочитаных сайтов, ведется в специальный файл.
    Формат файла: дата время название_сайта
"""


def log_site(site_name):
    logging.basicConfig(filename='tagcounter.log', level=logging.INFO, format='%(asctime)-20s %(message)s')
    logging.info(site_name)


def save_site_info(site):
    ret_dict = {}
    tags_info = ''

    site = get_site_by_synonym(site)
    site_url = 'http://' + site

    # get tags info and save in DB
    tags_dict = get_tag_count(site_url)

    # second domain | url | date of check | tags info
    db.add_record((site.split('.')[len(site.split('.'))-2], site_url, datetime.now(), pickle.dumps(tags_dict)))
    log_site(site)

    ret_dict['site'] = site
    ret_dict['tags'] = tags_dict

    return ret_dict


def show_site_info(site):
    ret_dict = {}

    site = get_site_by_synonym(site)
    site_url = 'http://' + site

    # get from DB the latest version of information
    if db.select_table(site_url):
        rec = db.select_table(site_url)[0]
        ret_dict['site'] = site
        ret_dict['tags'] = pickle.loads(rec[3])
    else:
        ret_dict['site'] = site
        ret_dict['tags'] = 'No INFO in DB'

    return ret_dict
