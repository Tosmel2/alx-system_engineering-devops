#!/usr/bin/python3
'''
export to JSON
'''

import json
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
    _id = data['employee']['id']
    _allData = []
    for task in data['tasks']:
        employee = {}
        employee['task'] = task['title']
        employee['completed'] = task['completed']
        employee['username'] = data['employee']['username']
        _allData.append(employee)
    _final = {_id: _allData}
    with open('{}.json'.format(_id), 'w') as f:
        json.dump(_final, f)


if __name__ == '__main__':
    getData(argv[1])
