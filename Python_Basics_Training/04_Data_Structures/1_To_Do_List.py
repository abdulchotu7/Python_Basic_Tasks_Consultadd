tasks = []

def add_task(task_name):
    tasks.append({"task": task_name, "done": False})
    print(f"Task '{task_name}' added.")

def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task index.")

def update_task(task_index, new_task_name):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["task"] = new_task_name
        print(f"Task updated to '{new_task_name}'.")
    else:
        print("Invalid task index.")

def mark_task_complete(task_name):
    for task in tasks:
        if task["task"] == task_name:
            task["done"] = True
            print(f"Task '{task_name}' marked as complete.")
            return
    print(f"Task '{task_name}' not found.")

def list_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

add_task("Study")
add_task("Workout")
list_tasks()
mark_task_complete("Study")
update_task(1, "Cook dinner")
remove_task(0)
list_tasks()