class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def __str__(self):
        return f"Task: {self.name}"
    
    def __repr__(self):
        return f"Task('{self.name}', subtasks={len(self.subtasks)})"
    
    def __len__(self):
        return len(self.subtasks)
    
    def __getitem__(self, index):
        return self.subtasks[index]
    
    def __bool__(self):
        return len(self.subtasks) > 0