# o aplicatie CLI ( command line interface ), de tip task manager
# permite utilizatorilor sa: create, update, delete
# class TaskManager
# decorator log_operation ( adica: daca se executa o functie, sa se logheze intr-un fisier log.txt : durata executiei -> in afara clasei
# functie view_tasks
# considerati ca aceste task-uri si citesc dintr-un fisier JSON ( se da acest fisier )

# aplicatia CLI : va avea un meniu care sa permite utilizatorului sa efectueze aceste operatii
# 1. Add task 2. Update task 3. Delete task 4. View task 5. Exit

import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'


def log_operation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} - {func.__name__} - {args[1:]}\n")
        return result

    return wrapper


class TaskManager:

    def __init__(self):
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "w") as file:
                json.dump([], file)

    def fetch_tasks(self):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)

    def save_tasks(self, tasks):
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)

    @log_operation
    def add_tasks(self, title, description, due_date, priority, status):
        tasks = self.fetch_tasks()
        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "status": status
        }
        tasks.append(new_task)
        self.save_tasks(tasks)
        print("Am adaugat task-ul cu succes!")

    @log_operation
    def update_task(self, index, title=None, description=None, due_date=None, priority=None, status=None):
        tasks = self.fetch_tasks()
        if 0 <= index < len(tasks):
            task = tasks[index]
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if due_date:
                task["due_date"] = due_date
            if priority:
                task["priority"] = priority
            if status:
                task["status"] = status

            self.save_tasks(tasks)
            print("Am actualizat task=ul cu succes!")
        else:
            print("Invalid task index")

    @log_operation
    def delete_task(self, index):
        tasks = self.fetch_tasks()
        if 0 <= index < len(tasks):
            del tasks[index]
            self.save_tasks(tasks)
            print("Am sters task-ul")
        else:
            print("Invalid task index")

    @log_operation
    def view_tasks(self):
        tasks = self.fetch_tasks()
        for index, task in enumerate(tasks):
            print(f"Task {index + 1}:")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")


def main():
    t1 = TaskManager()
    while True:
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = int(input("Alege ceva: "))
        if choice == 1:
            title = input("Enter title")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ")
            status = input("Enter status (Complete/Incomplete): ")
            t1.add_tasks(title, description, due_date, priority, status)
        elif choice == 2:
            index = int(input("Enter index")) - 1
            title = input("Enter title")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High/Medium/Low): ")
            status = input("Enter status (Complete/Incomplete): ")
            t1.update_task(index, title, description, due_date, priority, status)
        elif choice == 3:
            index = int(input("Enter index")) - 1
            t1.delete_task(index)
        elif choice == 4:
            t1.view_tasks()
        elif choice == 5:
            break
        else:
            print("Try again!")


if __name__ == "__main__":
    main()