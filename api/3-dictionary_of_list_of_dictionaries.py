#!/usr/bin/python3
"""
JSON output
"""

import json
import requests


url_users = "https://jsonplaceholder.typicode.com/users"
url_todos = "https://jsonplaceholder.typicode.com/todos"


def user_info():
    """ Doc """

    todos = requests.get(url_todos).json()
    users = requests.get(url_users).json()

    final_json = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        final_json[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(final_json, f)


if __name__ == "__main__":
    user_info()
