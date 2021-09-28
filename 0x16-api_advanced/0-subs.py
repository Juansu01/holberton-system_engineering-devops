#!/usr/bin/python3
"""This module consumes the reddit api"""

import requests


def number_of_subscribers(subreddit):
    my_header = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(
            subreddit), headers=my_header)
    if r.status_code != 200:
        return 0
    to_json = r.json()
    my_data = to_json['data']['subscribers']
    return my_data
