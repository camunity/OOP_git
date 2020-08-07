#### Task Class ####
"""
Hold information about each Task created by the user

"""

class Task:
        ### Data Object
    def __init__(self, name, task_id):
        self.name = name
        self.id = task_id

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"



#### TaskManager Class ####
"""
Manager object with CRUD functions related to Tasks

"""

class TaskManager:
    def __init__(self):
        pass