#!/usr/bin/python3
"""This module consumes the reddit api"""

import requests


def top_ten(subreddit):
    "Get the top 10 subreddit titles"
    my_header = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(
        'https://www.reddit.com/r/{}/top.json?limit=10'.format(
            subreddit), headers=my_header)
    if r.status_code != 200:
        return 0

    for val in r.json()['data']['children']:
        print(val['data']['title'])
