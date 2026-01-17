# Task 1: To-Do List Application

# Description: Build a simple command-line to-do list
# application. Users should be able to add, delete, mark
# as done, and list tasks.

# Objectives:
# a. Implement the ability to add, view, and delete tasks.
# b. Store the tasks in a file (either CSV or JSON format).
# c. Mark tasks as completed.
# d. Implement basic error handling (e.g., trying to delete a
#    task that doesn’t exist).

import json
import os

TODO_FILE = 'todo_list.json'


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("Error: Task index out of range.")


def mark_task_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
    else:
        print("Error: Task index out of range.")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['task']}")


def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            index = int(input("Enter the task index to delete: "))
            delete_task(index)
        elif choice == '3':
            index = int(input("Enter the task index to mark as completed: "))
            mark_task_completed(index)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()