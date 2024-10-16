import json
import datetime

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updatedAt': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(new_tasks)
    print("Task deleted successfully")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks)
            print("Task marked as in progress")
            return
    print("Task not found")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks(tasks)
            print("Task marked as done")
            return
    print("Task not found")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
    else:
        filtered_tasks = tasks
    for task in filtered_tasks:
        print(f"{task['id']}: {task['description']} (status: {task['status']})")

if __name__ == "__main__":
    while True:
        command = input("Enter a command (add, update, delete, mark-in-progress, mark-done, list, list-done, list-todo, list-in-progress, quit): ")
        if command == "quit":
            break
        elif command == "add":
            description = input("Enter task description: ")
            add_task(description)
        elif command == "update":
            task_id = int(input("Enter task ID: "))
            new_description = input("Enter new description: ")
            update_task(task_id, new_description)
        elif command == "delete":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
        elif command == "mark-in-progress":
            task_id = int(input("Enter task ID: "))
            mark_in_progress(task_id)
        elif command == "mark-done":
            task_id = int(input("Enter task ID: "))
            mark_done(task_id)
        elif command == "list":
            list_tasks()
        elif command == "list-done":
            list_tasks("done")
        elif command == "list-todo":
            list_tasks("todo")
        elif command == "list-in-progress":
            list_tasks("in-progress")
        else:
            print("Invalid command. Please try again.")