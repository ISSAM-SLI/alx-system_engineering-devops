#!/usr/bin/python3
'''
Module for recursively querying Reddit
API to get all hot articles' titles.
'''

import requests


def recurse(subreddit, hot_list=None, nxt=None):
    '''Recursively queries the Reddit API
       to get a list of all hot article titles.
       Returns a list of titles if successful,
       None if subreddit is invalid.
    '''
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'test'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': nxt}

    try:
        res = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)

        if res.status_code == 200:
            data = res.json().get('data', {})
            posts = data.get('children', [])
            nxt = data.get('after', None)

            for post in posts:
                hot_list.append(post['data'].get('title'))

            if nxt:
                # Recursive call to get the next page
                return recurse(subreddit, hot_list, nxt)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
