from leksikon.leksikon import var1, var2
from .goals import (create_goal, control_goals)


def show_menu(user_goals):
    """Create interface for customer"""
    if user_goals:
        print(var2)
        return True
    else:
        print(var1)
        return False
        

def user_choice(user_goals):
    while True:
        result = show_menu(user_goals)
        choice = int(input("Choice point: "))
        if result and choice == 1:
            control_goals(user_goals)
        elif not result and choice == 1:
            create_goal(user_goals)
        else:
            break
        
        