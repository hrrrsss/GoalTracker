from models.goal import Goal
from models.task import Task
from models.subtasks import Subtask


def distribution_goals(obj_user_goal: dict):
    result = []

    for goal in obj_user_goal:
        for name_goal, user_tasks in goal.items():
            added_goal = Goal(name_goal)
            for name_task, user_subtasks in user_tasks.items():
                added_task = Task(name_task)
                added_goal.tasks.append(added_task)
                for subtask in user_subtasks:
                    added_task.subtasks.append(subtask)
            result.append(added_goal)

    return result