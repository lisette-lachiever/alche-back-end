#!/usr/bin/python3
"""
Simple script to export an employee's TODO list to CSV.
"""

import csv
import requests
import sys


def main():
    emp_id = sys.argv[1]

    # Get user info
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    ).json()
    username = user.get("username")

    # Get tasks
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    ).json()

    # Open CSV file
    filename = "{}.csv".format(emp_id)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # Write each task
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()
