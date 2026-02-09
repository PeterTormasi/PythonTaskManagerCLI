import storage as storage

tasks = storage.load_tasks()

def add_task(taskname):
    tasks.append({
        "id":tasks[-1]["id"]+1 if len(tasks) > 0 else 1, 
        "name": taskname,
        "completed": False
        })

def print_tasks():
    if len(tasks) == 0: print("Nincs feladat!")
    for i in tasks:
        print(f"[{'✔' if i['completed'] == True else ' '}] {i['id']} - {i['name']}")

def mark_complete(taskname):
    for i in tasks:
        if i["name"] == taskname:
            i["completed"] = True

def delete_task(taskname):
    for i in tasks:
        if i["name"] == taskname:
            tasks.remove(i)

def save_tasks():
    storage.save_tasks(tasks)
