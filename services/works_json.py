import json


def load_json(filename):
    with open(filename, encoding="utf-8") as f:
        content = json.load(f)
    return content

def dump_json(filename, obj_with_goals: dict):
    
    if obj_with_goals:
        added_goals = dict()
        for goal in obj_with_goals:
            added_goals[goal.name] = dict()
            if goal:
                for task in goal:
                    added_goals[goal.name][task.name] = dict()
                    if task:
                        for subtask in task:
                            added_goals[goal.name][task.name][subtask.name] = [subtask.progress_for_calculate]
    
    result = [added_goals]
    

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)