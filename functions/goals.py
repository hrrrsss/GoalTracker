from models.goal import Goal
from leksikon.leksikon import c_g
from .tasks import control_tasks

def show_goals(user_goals):
    print()
    print("-"*50)
    if user_goals:
        for goal in range(1, len(user_goals)+1):
            print(f"{goal}. {user_goals[goal-1]}")
    else:
        print("Goals are empty")
    print("-"*50)


def create_goal(user_goals):
    name = input("Enter name of goal: ")
    new_goal = Goal(name)
    user_goals.append(new_goal)
    print(f"Goal {name} is created")


def control_goals(user_goals):
    while True:
        show_goals(user_goals)
        print(c_g)
        choice = int(input("Choice a point: "))
        if choice == 1:
            choice_goal = int(input("Choice goal: ")) - 1
            control_tasks(user_goals[choice_goal])
        elif choice == 2:
            create_goal(user_goals)
        elif choice == 3:
            choice_goal = int(input("Choice goal: ")) - 1
            del user_goals[choice_goal]
        else:
            break