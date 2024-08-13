#!/usr/bin/python3
'''
Module for querying Reddit API to count keywords in hot posts.
'''

import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, after=None, word_count=None):
    '''Function that recursively queries
    Reddit and counts keyword occurrences.'''
    if word_count is None:
        word_count = defaultdict(int)

    headers = {'User-Agent': 'test'}
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url = f"{base_url}?after={after}" if after else base_url

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            return None

        data = res.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after', None)

        for post in posts:
            title = post['data']['title'].lower()
            # Find words in the title
            words = re.findall(r'\b\w+\b', title)
            for word in words:
                if word in word_list:
                    word_count[word] += 1

        if after:
            count_words(subreddit, word_list, after, word_count)

        return word_count

    except requests.exceptions.RequestException:
        return None


def print_count(subreddit, word_list):
    '''Prints sorted keyword counts.'''
    word_list = [word.lower() for word in word_list]
    counts = count_words(subreddit, word_list)
    if counts is None:
        return

    sorted_counts = sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
