#!/usr/bin/python3
"""
Simple script to show TODO list progress of an employee
using the JSONPlaceholder API.
"""

import requests
import sys



if __name__ == "__main__":

     # Get employee ID from command line
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Get employee information
    user = requests.get(url.format(emp_id)).json()

    # Get todos for that employee
    todos = requests.get(url.format(emp_id)).json()

    # Employee name
    name = user.get("name")

    # Tasks
    total = len(todos)
    done = [t for t in todos if t.get("completed") is True]
    number_done = len(done)

    # Print first line
    print("Employee {} is done with tasks({}/{}):".format(
        name, number_done, total))

    # Print completed task titles
    for task in done:
        print("\t {}".format(task.get("title")))
