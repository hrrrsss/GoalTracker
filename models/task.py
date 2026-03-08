class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def __str__(self):
        return f"Task: {self.name}"