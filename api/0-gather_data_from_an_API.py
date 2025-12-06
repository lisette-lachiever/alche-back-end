#!/usr/bin/python3

import requests
import sys


def main():
    # Get employee ID from command line
    emp_id = sys.argv[1]

    # Get employee information
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(emp_id)).json()

    # Get todos for that employee
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)).json()

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


if __name__ == "__main__":
    main()

