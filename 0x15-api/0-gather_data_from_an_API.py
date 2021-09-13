#!/usr/bin/python3
"""This module returns information about an employee."""
import requests
import json
from sys import argv

users = requests.get("https://jsonplaceholder.typicode.com/users").json()
todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
user_tasks = []
completed_tasks = 0
total_tasks = 0
complete_tasks_list = []

for user in users:
    if user.get("id") == int(argv[1]):
        user_name = user.get("name")
for todo in todos:
    if todo.get("userId") == int(argv[1]):
        user_tasks.append(todo)
for task in user_tasks:
    if task.get("completed") is True:
        completed_tasks += 1
        complete_tasks_list.append(task.get("title"))
    total_tasks += 1
print("Employee {} is done with tasks({}/{})".format(
    user_name, completed_tasks, total_tasks))
for task in complete_tasks_list:
    print("\t {}".format(task))
