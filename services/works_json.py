import json

def load_json(filename):
    with open(filename, encoding="utf-8") as f:
        content = json.load(f)
    return content

def dump_json(filename, obj_with_goals: dict):
    result = dict()

    for goal in obj_with_goals:
        goal_name = goal.name
        result[goal_name] = {}
        for task in goal:
            task_name = task.name
            result[goal_name][task_name] = []
            for subtask in task:
                subtask_name = subtask
                result[goal_name][task_name].append(subtask_name)

    result = [result]

    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)