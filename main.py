from models.goal import Goal
from leksikon.leksikon import var1, var2

def show_menu(user_goals):
    """Create interface for customer"""
    if user_goals:
        print(var2)
    else:
        print(var1)

def create_goal(user_goals: list):
    """Create new goal"""
    
    name = input("Enter name of goal: ")
    deadline = input("You want to have a deadline? (y/n): ")
    if deadline in ("y", "Y"):
        deadline = input("Enter date of deadline: (__.__.____): ")
    else:
        deadline = None

    new_goal = Goal(name, deadline)
    user_goals.append(new_goal)

def user_choice(user_goals):
    while True:
        show_menu(user_goals)
        choice = int(input("Choice point: "))
        if choice == 1:
            create_goal(user_goals)
        elif choice == 2 and user_goals:
            print()
            for goal in user_goals:
                print(goal)
        else:
            break

def main():
    """Main function of programm"""
    user_goals = []

    user_choice(user_goals)

        

if __name__ == "__main__":
    main()