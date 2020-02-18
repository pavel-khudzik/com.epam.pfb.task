import yaml

"""
Для удобства работы, создать файл с синонимами в формате yaml. 
Данный файл для каждого сайта опредляет синоним, например: ydx: yandex.ru ggl: google.com

Для примера, к программе приложить файл с несколькими синонимами. 
Пользователи сами дложны иметь возможность добавлять, удалять данные из файла.
"""

def get_site_by_synonym(synonym):
    try:
        data = yaml.safe_load(open('tagcounter.yaml'))
    except FileNotFoundError:
        with open('tagcounter.yaml', 'a') as yf:
            pass

        data = yaml.safe_load(open('tagcounter.yaml'))

    return data.setdefault(synonym, None)

