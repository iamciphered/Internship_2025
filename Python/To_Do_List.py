#!/usr/bin/env python3

# Task 5: Simple To-Do List
# Allows users to add, view, and remove tasks

tasks = []

while True:
    print("\n=== To-Do List ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        if not tasks:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '2':
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
