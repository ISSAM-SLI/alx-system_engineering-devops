#!/usr/bin/python3
""" importing the necessary modules """

import requests
import sys
import json


def export_to_json():
    """Retrieves employee TODO list data and exports it in JSON format"""

    employee_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_data = response.json()

    username = employee_data.get('username')

    todo_url = (f'https://jsonplaceholder.typicode.com/users/'
                f'{employee_id}/todos')
    response = requests.get(todo_url)
    todos = response.json()

    tasks_data = []
    for todo in todos:
        task_info = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': username
        }
        tasks_data.append(task_info)

    data = {employee_id: tasks_data}
    file_name = f"{employee_id}.json"
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    export_to_json()
