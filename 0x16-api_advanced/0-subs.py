#!/usr/bin/python3
'''
Module for querying Reddit API to get subscriber count.
'''

import requests


def number_of_subscribers(subreddit):
    '''Queries the Reddit API and returns the number
       of subscribers for the given subreddit.
       Returns 0 if the subreddit is invalid or an error occurs.
    '''
    headers = {'User-Agent': 'test'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)

        if res.status_code == 200:
            data = res.json()
            subs = data.get('data', {}).get('subscribers', 0)
        else:
            subs = 0
    except requests.exceptions.RequestException:
        return 0

    return subs
