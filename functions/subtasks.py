from leksikon.leksikon import c_t

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

def control_subtasks(task):
    while True:
        show_subtasks(task)
        print(c_t)
        choice = int(input("Choice a point: "))
        if choice == 1:
            ...
        else:
            break