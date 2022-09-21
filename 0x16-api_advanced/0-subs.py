#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
of a given subreddit. If it is invalid return 0"""


import requests


def number_of_subscribers(subreddit):
    """Function that returns number of subs of a subreddit"""
    # Set the default URL strings
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)

    # Set user-agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Get the Reddit API response
    resp = requests.get(api_uri, headers=user_agent,
                        allow_redirects=False)

    # If the subreddit is invalid -> Return 0
    if resp.status_code in [302, 404]:
        return 0

    # If the subreddit is valid -> Return the sub number
    return resp.json().get('data').get('suscribers')
