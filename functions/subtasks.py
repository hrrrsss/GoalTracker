from leksikon.leksikon import c_t

def show_subtasks(subtasks):
    print()
    print("-"*50)
    if subtasks:
        for subtask in range(1, len(subtasks)+1):
            print(f"{subtask}. {subtasks[subtask-1]}")
        return True
    else:
        print("Subtasks are empty")
    print("-"*50)

def control_subtasks(task):
    while True:
        show_subtasks(task.subtasks)
        print(c_t)
        choice = int(input("Choice a point: "))
