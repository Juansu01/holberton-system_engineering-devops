#!/usr/bin/python3
"""This module returns information about an employee."""
if __name__ == "__main__":
    import requests
    import json
    from sys import argv
    import csv

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    user_tasks = []
    complete_tasks_list = []
    my_list = []
    my_dict = {}

    for user in users:
        if user.get("id") == int(argv[1]):
            user_name = user.get("name")
    for todo in todos:
        if todo.get("userId") == int(argv[1]):
            user_tasks.append(todo)
    for task in user_tasks:
        aux_dict = {}
        aux_dict['task'] = task.get('title')
        aux_dict['completed'] = task.get('completed')
        aux_dict['username'] = user_name
        my_list.append(aux_dict)

    my_dict[argv[1]] = my_list
    file = open("{}.json".format(argv[1]), "w", newline="")
    json.dump(my_dict, file)
    file.close()
