"""
Tagcounter program as a part of Python for beginners program

Run from console examples
    tagcounter --get "yandex.ru"   # count tags and save this information into DB
    tagcounter --view "yandex.ru"  # show information about this site form DB
Run GUI version
    tagcounter

Instead of use full names of sites synonyms are allowed.
List of synonyms and sites is stored in tagcounter.yaml
"""

import argparse
from utils.siteprocessing import save_site_info, show_site_info
from utils.guiapi import run_window


parser = argparse.ArgumentParser(description='Process commands from CM (--get|--view)')
parser.add_argument('--get')
parser.add_argument('--view')

args = parser.parse_args()
input_params = vars(args)


def print_info(dict):
    print('   site: {}'.format(dict['site']))
    print('   tags: {}'.format(dict['tags']))


# check action
if input_params.get('get'):  # receive tag info and save it in the DB
    print('START...')
    print_info(save_site_info(input_params['get']))
    print('...THIS INFORMATION SUCCESSFULLY STORED IN DB!')

elif input_params.get('view'):  # get tag info from DB and show
    print('START...')
    print_info(show_site_info(input_params['view']))
    print('...FINISH GETTING INFO!')

else:  # run gui version
    run_window()

