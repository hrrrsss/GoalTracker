from leksikon.leksikon import c_t
from models.task import Task
from .subtasks import control_subtasks

def show_tasks(tasks: list):
    print()
    print("-"*50)
    if tasks:
        for task in range(1, len(tasks)+1):
            print(f"{task}. {tasks[task-1]}")
        return True
    else:
        print("Tasks are empty")
    print("-"*50)


def create_task(goal):
    name = input("Enter a name for task: ")
    new_task = Task(name)
    goal.tasks.append(new_task)
    print("New task creates")


def control_tasks(goal):
    while True:
        show_tasks(goal.tasks)
        print(c_t)
        choice = int(input("Choice a point: "))
        if choice == 1:
            choice_task = int(input("Choice a task: ")) - 1
            control_subtasks(goal.tasks[choice_task])
        elif choice == 2:
            create_task(goal)
        elif choice == 3:
            choice_task = int(input("Choice a task: ")) - 1
            del goal.tasks[choice_task]
        else:
            break
        
