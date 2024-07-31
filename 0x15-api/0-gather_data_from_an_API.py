#!/usr/bin/python3

import sys
import requests


def display_todo():
    """Retrieves and prints the TODO list progress for a specified employee"""

    employee_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_data = response.json()

    employee_name = employee_data['name']

    todo_url = (f'https://jsonplaceholder.typicode.com/users/'
                f'{employee_id}/todos')
    response = requests.get(todo_url)
    todos = response.json()

    total_tasks = len(todos)
    completed_tasks = []
    for todo in todos:
        if todo['completed']:
            completed_tasks.append(todo['title'])
    completed_count = len(completed_tasks)

    print(f'Employee {employee_name} is done with tasks'
          f'({completed_count}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task}')


if __name__ == "__main__":
    display_todo()
