#!/usr/bin/python3
"""
place holder
"""


if __name__ == "__main__":

    import csv
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(argv[1]))
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(argv[1]))
    name = name.json()
    name = name[0]["username"]
    todos = todos.json()
    file_name = "{}.csv".format(argv[1])
    with open(file_name, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], name, todo['completed'], todo['title']])
