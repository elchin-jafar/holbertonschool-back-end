#!/usr/bin/python3
"""best module"""
import requests
import sys


def main():
    BASE_URL = "https://jsonplaceholder.typicode.com/"
    r_employee = requests.get("{}users/{}".format(BASE_URL, sys.argv[1]))
    EMPLOYEE_NAME = r_employee.json()["name"]

    r_todo = requests.get("{}todos".format(BASE_URL))

    result = list(filter(lambda x: x['userId'] == int(sys.argv[1]),
                         r_todo.json()))
    TOTAL_NUMBER_OF_TASKS = len(result)

    done = list(filter(lambda x: x["completed"] is True, result))
    NUMBER_OF_DONE_TASKS = len(done)
    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for todo in done:
        print("\t{}".format(todo['title']))


if __name__ == "__main__":
    main()
