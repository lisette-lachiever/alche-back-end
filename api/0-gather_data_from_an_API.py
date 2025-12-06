#!/usr/bin/python3
"""
Displays TODO list progress for a given employee
using the JSONPlaceholder API.
"""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: ./0-gather_data_from_an_API.py <employee_id>")

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(f"{base_url}users/{emp_id}").json()
    todos = requests.get(f"{base_url}todos?userId={emp_id}").json()

    name = user.get("name")

    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    completed_count = len(done_tasks)

    print(
    f"Employee {name} is done with tasks({completed_count}/{total_tasks}):"
)

    for task in done_tasks:
        print(f"\t {task.get('title')}")
