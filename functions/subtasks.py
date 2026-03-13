from leksikon.leksikon import c_s, view_s

from models.subtask import Subtask

def show_subtasks(task):
    print()
    print("-"*50)
    if task:
        for subtask in range(1, len(task)+1):
            print(f"{subtask}. {task[subtask-1]}")
        return True
    else:
        print("Subtasks are empty")
    print("-"*50)

def create_subtask(task):
    name = input("Enter a name for subtask: ")
    new_subtask = Subtask(name)
    task.subtasks.append(new_subtask)
    print("New subtask create")

def s(subtask):
    print()
    print(subtask.progress)
    while True:
        print(view_s)
        choice = int(input("Enter a point: "))
        
        if choice == 1:
            percent = int(input("Enter a percent of completion: "))
            subtask.progress = percent
            print(subtask.progress)
        else:
            break

def control_subtasks(task):

    while True:
        print(task.progress)
        show_subtasks(task)
        print(c_s)
        choice = int(input("Choice a point: "))
        if choice == 1:
            choice_subtask = int(input("Choice a subtask: ")) - 1
            s(task[choice_subtask])
        elif choice == 2:
            create_subtask(task)
        elif choice == 3:
            choice_subtask = int(input("Choice a subtask: ")) - 1
            del task.subtasks[choice_subtask]
        else:
            break