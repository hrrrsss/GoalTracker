from tkinter import *
from tkinter import ttk
from models.goal import Goal
from models.task import Task
from models.subtask import Subtask

class GoalTrackerInterface:
    def __init__(self, root, goals):
        self.root = root
        self.goals = goals
        self.main_frame = Frame(root)
        self.main_frame.pack(fill=BOTH, expand=True)
        self.show_goals()

    
    def create_goal(self):
        dialog = Toplevel(self.root)
        dialog.title("New Goal")
        dialog.geometry("300x150")
        dialog.resizable(False, False)

        Label(dialog, text="Goal name:", font=("Arial", 10)).pack(pady=5)
        entry = Entry(dialog, width=30, font=("Arial", 10))
        entry.pack(padx=10, pady=5)
        entry.focus()

        def save():
            name = entry.get().strip()
            if name:
                new_goal = Goal(name)
                self.goals.append(new_goal)
                dialog.destroy()
                self.show_goals()
            else:
                Label(dialog, text="Name cannot be empty!", fg="red").pack()
        
        btn_frame = Frame(dialog)
        btn_frame.pack(pady=10)

        Button(btn_frame, text="Save", command=save, width=10).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Cancel", command=dialog.destroy, width=10).pack(side=LEFT)


    def create_task(self, goal):
        dialog = Toplevel(self.root)
        dialog.title("New Task")
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        
        Label(dialog, text=f"Task for: {goal.name}", font=("Arial", 10)).pack(pady=5)
        Label(dialog, text="Task name:", font=("Arial", 10)).pack()
        
        entry = Entry(dialog, width=30, font=("Arial", 10))
        entry.pack(padx=10, pady=5)
        entry.focus()
        
        def save():
            name = entry.get().strip()
            if name:
                new_task = Task(name)
                goal.tasks.append(new_task)
                dialog.destroy()
                self.show_tasks(goal)
        
        btn_frame = Frame(dialog)
        btn_frame.pack(pady=10)
        
        Button(btn_frame, text="Save", command=save, width=10).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Cancel", command=dialog.destroy, width=10).pack(side=LEFT)


    def create_subtask(self, task):
        dialog = Toplevel(self.root)
        dialog.title("New Task")
        dialog.geometry("300x150")
        dialog.resizable(False, False)
        
        Label(dialog, text=f"Subtask for: {task.name}", font=("Arial", 10)).pack(pady=5)
        Label(dialog, text="Subtask name:", font=("Arial", 10)).pack()
        
        entry = Entry(dialog, width=30, font=("Arial", 10))
        entry.pack(padx=10, pady=5)
        entry.focus()
        
        def save():
            name = entry.get().strip()
            if name:
                new_subtask = Subtask(name)
                task.subtasks.append(new_subtask)
                dialog.destroy()
                self.show_subtasks(task)
        
        btn_frame = Frame(dialog)
        btn_frame.pack(pady=10)
        
        Button(btn_frame, text="Save", command=save, width=10).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Cancel", command=dialog.destroy, width=10).pack(side=LEFT)
        
    
    def show_goals(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        Label(self.main_frame, text="My Goals", font=("Arial", 16)).pack(pady=10)

        goals_frame = Frame(self.main_frame)
        goals_frame.pack(expand=True, fill=BOTH, pady=20)

        if self.goals:
        
            buttons_frame = Frame(goals_frame)
            buttons_frame.pack(expand=True)

            for goal in self.goals:
                btn = Button(buttons_frame,
                            text=goal.name,
                            font=("Arial", 14),
                            width=20,
                            height=2,
                            command=lambda g=goal: self.show_tasks(g))
                btn.pack(pady=10)
        else:
            info = Label(self.goals_frame, text="Goals empties", font=("Arial", 14)).pack(expand=True)

        btn_new = Button(self.main_frame, 
                         text="+ New goal", 
                         font=("Arial", 12),
                         width=15,
                         command=lambda: self.create_goal())
        btn_new.pack()

    
    def show_tasks(self, goal):
        self.current_goal = goal

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        Label(self.main_frame, text="My Tasks", font=("Arial", 16)).pack(pady=10)

        tasks_frame = Frame(self.main_frame)
        tasks_frame.pack(expand=True, fill=BOTH, pady=20)

        if goal.tasks:
            buttons_frame = Frame(tasks_frame)
            buttons_frame.pack(expand=True)
            
            for task in goal.tasks:
                btn = Button(buttons_frame,
                            text=task.name,
                            font=("Arial", 14),
                            width=20,
                            height=2,
                            command=lambda t=task: self.show_subtasks(t))
                btn.pack(pady=10)
        else:
            info = Label(tasks_frame, text="No tasks yet", font=("Arial", 12))
            info.pack(expand=True)

        control_frame = Frame(self.main_frame)
        control_frame.pack(side=BOTTOM, pady=20)

        btn_new = Button(control_frame, text="+ New task", 
                        font=("Arial", 12),
                        width=15,
                        command=lambda: self.create_task(goal))
        btn_new.pack(pady=5)

        back_btn = Button(control_frame, text="← Back to goals", 
                        font=("Arial", 12),
                        width=15,
                        command=self.show_goals)
        back_btn.pack(pady=5)


    def show_subtasks(self, task):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        Label(self.main_frame, text="My Subtasks", font=("Arial", 16)).pack(pady=10)

        subtasks_frame = Frame(self.main_frame)
        subtasks_frame.pack(expand=True, fill=BOTH, pady=20)

        if task.subtasks:
            buttons_frame = Frame(subtasks_frame)
            buttons_frame.pack(expand=True)
            
            for subtask in task.subtasks:
                btn = Button(buttons_frame,
                            text=subtask.name,
                            font=("Arial", 14),
                            width=20,
                            height=2)
                btn.pack(pady=10)
        else:
            info = Label(subtasks_frame, text="No subtasks yet", font=("Arial", 12))
            info.pack(expand=True)

        control_frame = Frame(self.main_frame)
        control_frame.pack(side=BOTTOM, pady=20)

        btn_new = Button(control_frame, text="+ New Subtask", 
                        font=("Arial", 12),
                        width=15,
                        command=lambda: self.create_subtask(task))
        btn_new.pack(pady=5)

        back_btn = Button(control_frame, text="← Back to tasks", 
                        font=("Arial", 12),
                        width=15,
                        command=lambda: self.show_tasks(self.current_goal))
        back_btn.pack(pady=5)