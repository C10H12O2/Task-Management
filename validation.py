from datetime import datetime


def validate_task_title(title):
    if not title or not title.strip():
        print("Error: Task title cannot be empty.")
        return False

    if len(title.strip()) < 3:
        print("Error: Task title must be at least 3 characters long.")
        return False

    return True


def validate_task_description(description):
    None


def validate_due_date(due_date):
    None
