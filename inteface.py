from tkinter import *
from tkinter import ttk
from models.goal import Goal  # твой класс Goal
from models.task import Task  # твой класс Task

# Создаем окно
root = Tk()
root.title("GoalTracker")
root.geometry("500x400")

# Вместо списка строк - список ОБЪЕКТОВ Goal
goals = [
    Goal("Выучить Python"),
    Goal("Сделать проект"),
    Goal("Найти работу")
]

# Добавим пару задач для первой цели
goals[0].tasks.append(Task("Изучить основы"))
goals[0].tasks.append(Task("Сделать мини-проект"))

# Главный контейнер
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

def show_goals():
    """Показывает экран со списком целей"""
    # Очищаем контейнер
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    # Заголовок
    title = Label(main_frame, text="МОИ ЦЕЛИ", font=("Arial", 16))
    title.pack(pady=10)
    
    # Кнопки целей - теперь goal это объект, а не строка
    for goal in goals:
        btn = Button(main_frame, 
                    text=goal.name,  # берем name у объекта Goal
                    font=("Arial", 12),
                    width=30,
                    command=lambda g=goal: show_tasks(g))  # передаем объект
        btn.pack(pady=5)
    
    # Кнопка новой цели
    btn_new = Button(main_frame, text="+ Новая цель", command=create_goal)
    btn_new.pack(pady=20)

def show_tasks(goal):
    """Показывает экран с задачами выбранной цели"""
    # Очищаем контейнер
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    # Заголовок с названием цели
    title = Label(main_frame, text=f"ЦЕЛЬ: {goal.name}", font=("Arial", 16))
    title.pack(pady=10)
    
    # Если есть задачи - показываем их
    if goal.tasks:
        for task in goal.tasks:
            btn = Button(main_frame,
                        text=task.name,
                        font=("Arial", 12),
                        width=30)
            btn.pack(pady=5)
    else:
        # Если задач нет
        info = Label(main_frame, text="Нет задач", font=("Arial", 12))
        info.pack(pady=20)
    
    # Кнопка новой задачи
    btn_new = Button(main_frame, text="+ Новая задача", 
                    command=lambda: create_task(goal))
    btn_new.pack(pady=10)
    
    # Кнопка "Назад"
    back_btn = Button(main_frame, text="← Назад к целям", command=show_goals)
    back_btn.pack(pady=10)

def create_goal():
    """Создает новую цель (пока просто тест)"""
    new_goal = Goal("Новая цель")
    goals.append(new_goal)
    show_goals()  # обновляем экран

def create_task(goal):
    """Создает новую задачу для цели"""
    new_task = Task("Новая задача")
    goal.tasks.append(new_task)
    show_tasks(goal)  # обновляем экран

# Запускаем
show_goals()
root.mainloop()