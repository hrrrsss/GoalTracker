from .task import Task

class Goal:
    def __init__(self, name, deadline=None):
        self.name = name
        self.deadline = deadline
        self.tasks = []
        self.create_date = None

    @property
    def progress(self):
        if not self.tasks:
            return 0
        total = sum([t.progress_for_calculate for t in self.tasks])
        result = total / len(self.tasks)
        return f"\nProgress: {result}%"

    def __str__(self):
        return f"Goal: {self.name}"
    
    def __repr__(self):
        return f"Goal('{self.name}', tasks={len(self.tasks)})"
    
    def __len__(self):
        return len(self.tasks)
    
    def __getitem__(self, index):
        return self.tasks[index]
    
    def __bool__(self):
        return len(self.tasks) > 0