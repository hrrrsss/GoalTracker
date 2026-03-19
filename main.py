from tkinter import Tk
from inteface import GoalTrackerInterface
from common.load_dump_pickle import load, dump



def main():
    """Main function of programm"""
    filename = "goals.pkl"
    user_goals = load(filename)

    root = Tk()
    root.title("GoalTracker")
    root.geometry("900x700")

    app = GoalTrackerInterface(root, user_goals)

    root.mainloop()

    
    dump(filename, user_goals)


        

if __name__ == "__main__":
    main()