#!/usr/bin/python
""" Script to return the top posts from reddit in a specified sub reddit.
    Default number of posts returned is 5, can be changed with the --limit argument.
    Usage:
        python top_posts.py do -l 10
        python top_posts.py py
        python top_posts.py toronto -l 7
"""
import argparse
import datetime
import requests
from requests.exceptions import HTTPError

parser = argparse.ArgumentParser(
    description='Get MS Graph Permission details.')

parser.add_argument(
    'sr',  help="Enter the sub reddit to check. ans = Ansible, do = DevOps, py = Python, ps = PowerShell, pfc = Personal Finance Canada or write the fullname of the sub reddit.")
parser.add_argument('-l', '--limit', help='Limit number of posts to return', type=int)
args = parser.parse_args()


limit = 5

if args.limit is not None:
    limit = args.limit

url = 'https://www.reddit.com/r/'
suffix = f'/top/.json?limit={limit}'

subs = {
    'ans': 'Ansible',
    'do': 'DevOps',
    'py': 'Python',
    'ps': 'PowerShell',
    'pfc': 'PersonalFinanceCanada'
    }

if args.sr in subs:
    sub_reddit = subs[args.sr]
else:
    sub_reddit = args.sr

try:
    response = requests.get(
        url + sub_reddit + suffix,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
    )
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

if response.status_code != 200:
    print('Status code was not 200, status is: {}'.format(response.status_code))
    exit()

itemList = response.json()['data']['children']

for item in itemList:
    created = datetime.datetime.fromtimestamp(item['data']['created_utc'])
    print('\n' + item['data']['title'])
    print(
        f"Score: {item['data']['score']} Upvote Ratio: {item['data']['upvote_ratio']} Comments: {item['data']['num_comments']}")
    print(f"Created: {created:%Y-%m-%d %H:%M:%S}")
    print(item['data']['url'])
