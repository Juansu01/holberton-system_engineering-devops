#!/usr/bin/python3
"""This module returns information about an employee."""
if __name__ == "__main__":
    import requests
    import json

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    my_users = {}
    usernames = {}
    for user in users:
        user_id = user.get("id")
        my_users[user_id] = []
        usernames[user_id] = user.get("username")

    for todo in todos:
        my_id = todo.get("userId")
        aux_dict = {}
        aux_dict['task'] = todo.get('title')
        aux_dict['completed'] = todo.get('completed')
        aux_dict['username'] = usernames.get(my_id)
        my_users[my_id].append(aux_dict)

    file = open("todo_all_employees.json", "w", newline="")
    json.dump(my_users, file)
    file.close()
