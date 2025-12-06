#!/usr/bin/python3
"""
Script to export an employee's TODO list in JSON format.
"""

import json
import requests
import sys


def main():
    emp_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user = requests.get(user_url).json()
    username = user.get("username")

    todos = requests.get(todos_url, params={"userId": emp_id}).json()

    data = {
        emp_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    filename = "{}.json".format(emp_id)

    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
