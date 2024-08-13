#!/usr/bin/python3
'''
Module for querying Reddit API to get subscriber count.
'''

import requests

def number_of_subscribers(subreddit):
    '''Queries the Reddit API and returns the number of subscribers for the given subreddit.
       Returns 0 if the subreddit is invalid or an error occurs.
    '''
    headers = {'User-Agent': 'test'}
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers=headers)
    try:
        subs = res.json()['data']['subscribers']
    except Exception:
        return 0
    return subs
