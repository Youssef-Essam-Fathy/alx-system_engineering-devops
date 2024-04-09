#!/usr/bin/python3
'''
Importing a module
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Queries  the Reddit API
    and returns the number of subscribers
    '''
    url = "https://www.reddit.com/r/{}/about.json"
    sub_info = requests.get(url.format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        return 0
    return sub_info.json().get("data").get("subscribers")
