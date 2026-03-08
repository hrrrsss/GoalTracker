from functions.first import user_choice

from models.goal import Goal


def main():
    """Main function of programm"""
    user_goals = [Goal("lolka")]

    user_choice(user_goals)
        

if __name__ == "__main__":
    main()