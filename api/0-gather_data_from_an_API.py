#!/usr/bin/python3
"""returns information about his/her"""


from requests import get
from sys import argv


if __name__=="__main__":

    user_id = argv[1]
    url_user = get("https://jsonplaceholder.typicode.com/users").json()
    url_todos = get("https://jsonplaceholder.typicode.com/todos").json()


    total_tasks = 0
    task_done = 0
    list_tasks = []

    for task in url_todos():
        total_tasks += 1
        if task['completed'] is True:
            task_done += 1
            list_tasks.append(task['title'])

    employee = url_user.json()['name']

    print("Employee {} is done with tasks({}/{}):".format(task_done, total_tasks))