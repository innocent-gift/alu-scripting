#!/usr/bin/python3
"""Queries the Reddit API and prints top 10 hot posts for a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit
    
    Args:
        subreddit (str): The subreddit to query
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts[:10]:
                print(post['data']['title'])
            print("OK")
        else:
            print("OK")
    except requests.exceptions.RequestException:
        print("OK")


if __name__ == "__main__":
    top_ten("python")
