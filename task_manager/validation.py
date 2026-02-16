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
    if description and len(description) > 400:
        print("Error: Task description cannot exceed 400 characters.")
        return False
    
    if description and len(description) < 10:
        print("Error: Task description must be at least 10 characters long.")
        return False
    
    return True


def validate_due_date(due_date):
    if not due_date or not due_date.strip():
        print("Error: Due date can't be empty.")
        return False
    
    try:
       date_input = datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
        return False

    if date_input.date() < datetime.now().date():
        print("Error: Due date can't be in the past.")
        return False

    return True