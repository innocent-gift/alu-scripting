#!/usr/bin/python3
"""Query the Reddit API and print top 10 hot posts for a subreddit"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, print None.
    
    Args:
        subreddit (str): The name of the subreddit to query
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if subreddit exists (status 200) or doesn't exist (status 404)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
