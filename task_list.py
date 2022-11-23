tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


#Print a list of uncompleted tasks
def uncompleted_tasks():
    list_uncompleted_tasks = []
    for task in tasks:
        if task["completed"] == False:
            list_uncompleted_tasks.append(task["description"])

    print(list_uncompleted_tasks)

uncompleted_tasks()

#Print a list of completed tasks
def completed_tasks():
    list_of_completed_tasks = []
    for task in tasks:
        if task["completed"] == True:
            list_of_completed_tasks.append(task["description"])

    print(list_of_completed_tasks)

completed_tasks()

#Print a list of all task descriptions

def task_descriptions():
    list_of_descriptions_of_tasks = []
    for task in tasks:
        list_of_descriptions_of_tasks.append(task["description"])

    print(list_of_descriptions_of_tasks)

task_descriptions()

#Print a list of tasks where time_taken is at least a given time

def minutes_taken():
    list_of_tasks_that_take_longer = []
    for task in tasks:
        if task ["time_taken"] > 25:
            list_of_tasks_that_take_longer.append(task["description"])

    print(list_of_tasks_that_take_longer)

minutes_taken()

#Print any task with a given description

def description_given():
    description_to_print = []
    for task in tasks:
        if task ["description"] == "Walk Dog":
            description_to_print.append(task["description"])

    print(description_to_print)

description_given()


#Given a description update that task to mark it as complete.

