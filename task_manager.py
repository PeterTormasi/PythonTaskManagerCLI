import storage as storage

def add_task(taskname):
    storage.add_task(taskname)

def print_tasks():
    tasks = storage.load_tasks()
    if len(tasks) == 0: print("Nincs feladat!")
    for i in tasks:
        print(f"[{'✔' if i[2] == 1 else ' '}] {i[0]} - {i[1]}")

def mark_complete(task_id):
    storage.complete_task(task_id)

def delete_task(task_id):
    storage.delete_task(task_id)
