#!/usr/bin/python3
"""
Export all employees' TODO data to JSON.
"""

import json
import requests


def main():
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()

    data = {}

    for user in users:
        uid = user.get("id")
        username = user.get("username")

        user_tasks = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
            }
            for t in todos if t.get("userId") == uid
        ]

        data[uid] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
