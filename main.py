from functions.first import user_choice

from models.goal import Goal
from services.works_json import load_json, dump_json

from common.distibution_goals import distribution_goals


def main():
    """Main function of programm"""
    filename = "MyGoals.json"
    
    load_user_goals = load_json(filename)

    user_goals = distribution_goals(load_user_goals)

    user_choice(user_goals)
    
    dump_json(filename, user_goals)
        

if __name__ == "__main__":
    main()