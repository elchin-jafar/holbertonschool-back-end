#!/usr/bin/python3
"""
Python script to export data in the JSON fromat
"""
import json
import requests


def export_to_json():
    """
    Fethces and processes user and TODO list data for the provided ID.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/"

    user = requests.get(user_url).json()
    json_dict = {}
    for usr in user:
        tasks_list = []
        Id = usr['id']
        tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={Id}"
        tasks = requests.get(tasks_url).json()
        user_name = usr['username']

        for task in tasks:
            tasks_dict = {}
            tasks_dict['username'] = user_name
            tasks_dict['task'] = task['title']
            tasks_dict['completed'] = task['completed']
            tasks_list.append(tasks_dict)

        json_dict[Id] = tasks_list

    with open('todo_all_employees.json', "w") as js_file:
        json.dump(json_dict, js_file, indent=4)


if __name__ == "__main__":
    export_to_json()