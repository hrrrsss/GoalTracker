class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []
        self.__progress = 0

    @property
    def progress_for_calculate(self):
        return self.__progress

    @property
    def progress(self):
        if not self.subtasks:
            return 0
        total = sum([p.progress_for_calculate for p in self.subtasks])
        result = total / len(self.subtasks)
        self.__progress = result
        return f"\nProgress: {result}%"

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