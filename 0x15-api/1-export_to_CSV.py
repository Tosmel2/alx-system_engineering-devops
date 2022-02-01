#!/usr/bin/python3
'''
export to CSV
'''

import csv
import requests
from sys import argv


def getData(id):
    '''get data  adn export of employee'''
    URL = 'https://jsonplaceholder.typicode.com/'
    ENDPOINT = URL + 'users/{}'.format(id)
    employee = requests.get(ENDPOINT).json()
    TASKENDPOINT = URL + 'todos?userId={}'.format(employee['id'])
    tasks = requests.get(TASKENDPOINT).json()
    data = {"employee": employee, "tasks": tasks}
    with open('{}.csv'.format(argv[1]), 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        _username = data['employee']['username']
        _id = data['employee']['id']
        for task in data['tasks']:
            w.writerow([_id, _username, task['completed'],
                        task['title']
                        ])


if __name__ == '__main__':
    getData(argv[1])
