#!/usr/bin/python3
'''
Module for querying Reddit API to get top 10 hot posts.
'''

import requests


def top_ten(subreddit):
    '''Queries the Reddit API and prints the titles of
       the first 10 hot posts for the given subreddit.
       Prints None if the subreddit is invalid or an error occurs.
    '''
    headers = {'User-Agent': 'test'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)

        if res.status_code == 200:
            data = res.json().get('data', {}).get('children', [])

            for post in data[:10]:
                print(post['data'].get('title'))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
