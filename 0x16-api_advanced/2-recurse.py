#!/usr/bin/python3
"""This module consumes the reddit api"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    "Get the top 10 subreddit titles"
    my_header = {'User-agent': 'Mozilla/5.0'}
    my_param = {'after': after}
    r = requests.get(
        'https://www.reddit.com/r/{}/hot.json?limit=100'.format(
            subreddit), headers=my_header, params=my_param)
    if r.status_code == 404:
        return None
    after = r.json().get('data').get('after')
    for val in r.json()['data']['children']:
        hot_list.append(val["data"]['title'])
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
