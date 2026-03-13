class Subtask:
    def __init__(self, name):
        self.name = name
        self.__progress = 0
    
    @property
    def progress_for_calculate(self):
        return self.__progress

    @property
    def progress(self):
        return f"Progress: {self.__progress}%"
    
    @progress.setter
    def progress(self, value):
        if isinstance(value, int) and self.__progress + value <= 100:
            self.__progress += value
        else:
            print("Value shoud be a integer num and sum not should be above 100")

    def __str__(self):
        return f"Subtask: {self.name}"
    
    def __repr__(self):
        return f"Subtask: {self.name}"