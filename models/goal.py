from .task import Task

class Goal:
    def __init__(self, name, deadline=None):
        self.name = name
        self.deadline = deadline
        self.tasks = [Task("MyTask")]
        self.create_date = None

    def __str__(self):
        return f"Goal: {self.name}"