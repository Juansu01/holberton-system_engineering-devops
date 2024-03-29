#!/usr/bin/python3
"""This module consumes the reddit api"""

import requests


def top_ten(subreddit):
    "Get the top 10 subreddit titles"
    my_header = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(
        'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
            subreddit), headers=my_header)
    if r.json().get('message') == "Not Found":
        print("None")
    else:
        for val in r.json()['data']['children']:
            print(val['data']['title'])
