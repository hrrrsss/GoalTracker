from functions.first import user_choice

from models.goal import Goal
from services.works_json import load_json, dump_json

from common.distibution_goals import distribution_goals

import pickle


def main():
    """Main function of programm"""
    filename = "MyGoals.json"

    with open("goals.pkl", 'rb') as f:
        user_goals = pickle.load(f)

    user_choice(user_goals)

    with open("goals.pkl", 'wb') as f:
        pickle.dump(user_goals, f)
        

if __name__ == "__main__":
    main()