#!/usr/bin/python3
"""
Queries the reddit API and
returns the number of subscribers
for a given subreddit.
If invalid subreddit is given,
function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
"""Returns the total subscribers
for a given subreddit.
"""
    # Set the default URL strings
    base_url = 'https://www.reddit.com'
    api_url = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)
    # Set an User-Agent
    user_agent = {'User-Agent': 'Python/request'}

    # Get the Response of the reddit API
    res = requests.get(api_url, headers=user_agent,
                       allow_redirects=False)

    # Checks if the subreddit is invalid
    if res.status_code in [302, 404]
       return 0

    # Returns the total subscribers
    return res.json().get('data').get('subscribers')
