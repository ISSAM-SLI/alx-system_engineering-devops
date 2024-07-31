#!/usr/bin/python3
""" Export employee tasks to a CSV file """

import csv
import requests
import sys


def export_to_csv():
    """Fetches tasks for an employee and exports them to a CSV file."""

    employee_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_data = response.json()

    # Extract employee details
    username = employee_data['username']

    todo_url = (f'https://jsonplaceholder.typicode.com/users/'
                f'{employee_id}/todos')
    response = requests.get(todo_url)
    todos = response.json()

    # Define CSV file name
    file_name = f"{employee_id}.csv"

    # Write data to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow(
                [employee_id, username, todo['completed'], todo['title']])


if __name__ == "__main__":
    export_to_csv()
