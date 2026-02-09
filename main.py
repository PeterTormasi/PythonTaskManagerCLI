import task_manager as taskmanager

while (True):
    print("=== TASK TRACKER === \n1 - Új feladat\n2 - Feladatok listázása\n3 - Késznek jelöl\n4 - Feladat törlése\n5 - Kilépés")
    action = input("")

    if action == "1": 
        taskmanager.add_task(input("Feladat neve: "))
    elif action == "2":
        taskmanager.print_tasks()
    elif action == "3":
        taskmanager.mark_complete(input("Feladat neve: "))
    elif action == "4": 
        taskmanager.delete_task(input("Feladat neve: "))
    elif action == "5":
        taskmanager.save_tasks()
        break
