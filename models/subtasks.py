class Subtask:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Subtasks: {self.name}"