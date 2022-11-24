tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


#Print a list of uncompleted tasks
def get_uncompleted_tasks(list_of_tasks):
    uncompleted_tasks = []
    for task in list_of_tasks:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

print(get_uncompleted_tasks(tasks))   

get_uncompleted_tasks(tasks)

#Print a list of completed tasks
def get_completed_tasks(list_of_tasks):
    completed_tasks = []
    for task in list_of_tasks:
        if task["completed"] == True:
            completed_tasks.append(task)
        return completed_tasks

print(get_completed_tasks(tasks))


get_completed_tasks()

#Print a list of all task descriptions

# def task_descriptions():
    # descriptions_of_tasks = []
    # for task in tasks:
        # list_of_descriptions_of_tasks.append(task["description"])

    # print(list_of_descriptions_of_tasks)

# task_descriptions()

#Print a list of tasks where time_taken is at least a given time

def get_tasks_taking_longer_than(list_of_tasks, time):
    found_tasks = []
    for task in list_of_tasks:
        if task["time_take"] >= time:
            found_tasks.append(task)

    return found_tasks



print(get_tasks_taking_longer_than(tasks))    

get_tasks_taking_longer_than()

tasks_lasting_at_least_30 = get_tasks_taking_longer_than(tasks, 30)
print(get_uncompleted_tasks(tasks_lasting_at_least_30))

#def minutes_taken():
#   list_of_tasks_that_take_longer = []
    #for task in tasks:
        #if task ["time_taken"] > 25:
            # list_of_tasks_that_take_longer.append(task["description"])

#    print(list_of_tasks_that_take_longer)

# minutes_taken()

#Print any task with a given description

#def description_given():
    #description_to_print = []
    # for task in tasks:
        # if task ["description"] == "Walk Dog":
            # description_to_print.append(task["description"])

    # print(description_to_print)

# description_given()


#Given a description, update that task to mark it as complete.

def get_task_with_description(list_of_tasks, description):
    #found_task = None
    for task in list_of_tasks:
        if task["description"] == description:
            return task
    
    return None

print(get_task_with_description(tasks, "Make dinner"))

def mark_task_as_complete(list_of_tasks, description):
    task = get_task_with_description(list_of_tasks, description)
    task ["completed"] = True

print(get_task_with_description(tasks, "Wash Dishes"))

mark_task_as_complete(tasks, "Wash Dishes")
print(get_task_with_description(tasks,"Wash Dishes"))
