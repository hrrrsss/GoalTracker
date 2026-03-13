from models.goal import Goal
from models.task import Task
from models.subtask import Subtask


def distribution_goals(obj_user_goal: dict):
    "Distribution of Python objects into different classes"

    result = []

    if obj_user_goal:
        for goal in obj_user_goal:
                for goal_name, tasks in goal.items():
                        goal_instance = Goal(goal_name)
                        if goal[goal_name]:
                            for task_name, subtasks in tasks.items():
                                task_instance = Task(task_name)
                                if tasks[task_name]:
                                    for subtask_name, subtask_data in subtasks.items():
                                        subtask_instance = Subtask(subtask_name)
                                        subtask_instance.progress = subtask_data[0]
                                    task_instance.subtasks.append(subtask_instance)
                                goal_instance.tasks.append(task_instance)
                        result.append(goal_instance)

    return result