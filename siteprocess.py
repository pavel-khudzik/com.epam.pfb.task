from html.parser import HTMLParser
import requests

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_dict = {}

    def handle_starttag(self, tag, attrs):
        self.tag_dict[tag] = self.tag_dict.setdefault(tag, 0) + 1


def get_tag_count(site):
    site = 'http://' + site

    parser = MyHTMLParser()

    try:
        parser.feed(requests.get(site).text)
        return parser.tag_dict
    except Exception:
        parser.tag_dict['ERROR'] = "{} can't be reached!".format(site)




