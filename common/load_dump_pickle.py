import pickle

def load(filename):
    with open(filename, "rb") as f:
        try:
            user_goals = pickle.load(f)
            return user_goals
        except:
            print("Load Error!")
    

def dump(filename, usergoals):
    with open(filename, "wb") as f:
        try:
            pickle.dump(usergoals, f)
        except:
            print("Dump Error!")