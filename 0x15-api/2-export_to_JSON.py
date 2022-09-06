#!/usr/bin/python3
"""Exports to a json file"""
import json
from sys import argv
import requests


if __name__ == '__main__':
    id = argv[1]
    us_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tod_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

    resp_todo = requests.get(tod_url).json()
    resp_user = requests.get(us_url).json()

    with open('{}.json'.format(id), 'w') as js:
        tsk = []
        for r in resp_todo:
            tsk.append({'task': r.get('title'),
                        'completed': r.get('completed'),
                        'username': resp_user.get('username')})
        info = {"{}".format(id): tsk}
        json.dump(info, js)
