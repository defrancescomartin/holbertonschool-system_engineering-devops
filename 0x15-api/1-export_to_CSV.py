

#!/usr/bin/python3
"""Exports results to an csv file"""
import csv
from sys import argv
import requests


if __name__ == '__main__':
    id = argv[1]
    us_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tod_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)

    resp_todo = requests.get(tod_url).json()
    resp_user = requests.get(us_url).json()

    with open('{}.csv'.format(id), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for x in resp_todo:
            y = [id, resp_user.get('username'),
                 x.get('completed'),
                 x.get('title')]
            y = [str(value) for value in y]
            csvwriter.writerow(y)
