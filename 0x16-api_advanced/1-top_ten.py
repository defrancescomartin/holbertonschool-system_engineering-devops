#!/usr/bin/python3
"""function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    # Set default URL Strings
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    # Set user-agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Set limit of Query Strings to be requested
    payload = {'limit': '10'}

    # Get the Reddit API response
    resp = requests.get(api_uri, headers=user_agent,
                        params=payload, allow_redirects=False)

    # If the subreddit is invalid -> Return 0
    if resp.status_code in [302, 404]:
        print('None')
    else:
        resp_json = resp.json()

        if resp_json.get('data') and resp_json.get('data').get('children'):
            # Get the 10 hot posts of the given subreddit
            hot_posts = resp_json.get('data').get('children')

            # Print all the 10 hot posts titles
            for post in hot_posts:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
