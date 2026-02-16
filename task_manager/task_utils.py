from datetime import datetime

# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# Define tasks list
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return
    if not validate_task_description(description):
        return
    if not validate_due_date(due_date):
        return

    task = {
        "title": title.strip(),
        "description": description.strip() if description else "",
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    print("Task has been added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Error: Invalid task number.")
        return

    if tasks[index]["completed"]:
        print(f"Task '{tasks[index]['title']}' is already marked as complete.")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]

    if not pending_tasks:
        print("\nYou've got no pending tasks!!!")
        return

    print("\n" + "=" * 60)
    print("Pending Tasks:")
    print("=" * 60)

    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"\nTask #{i+1}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Status: Pending")

    print("=" * 60)


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    None
    return progress
