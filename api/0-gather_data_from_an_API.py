#!/usr/bin/python3

import requests
from sys import argv

if __name__=="__main__":
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")

    