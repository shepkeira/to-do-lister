import json


light_pink = "#EABFCB"
grey_pink = "#C191A1"
dark_pink = "#A4508B"
light_blue = "#5F0A87"
dark_blue = "#2F004F"
projects = []


def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()


def reset():
    print("reset")
    #delete everything from .txt doc


class Task:
    def __init__(self, title, due_date, description, urgent, important, project):
        self.title = title
        self.due_date = due_date
        self.description = description
        self.urgent = urgent
        self.important = important
        self.project = project
    def print(self):
        print("\tTitle: ", self.title)
        print("\t\tDue Date: ", self.due_date)
        print("\t\tDescription: ", self.description)
        print("\t\tUrgent: ", self.urgent)
        print("\t\tImportant: ", self.important)


class Project:
    def __init__(self, title, due_date, description, urgent, important, tasks):
        self.title = title
        self.due_date = due_date #TODO 2: make into date format to use later
        self.description = description
        self.urgent = urgent
        self.important = important
        self.tasks = tasks

    def __init__(self, title, due_date, description, urgent, important):
        self.title = title
        self.due_date = due_date #TODO 1: make into date format to use later
        self.description = description
        self.urgent = urgent
        self.important = important
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def print(self):
        print("Title: ", self.title)
        print("\tDue Date: ", self.due_date)
        print("\tDescription: ", self.description)
        print("\tUrgent: ", self.urgent)
        print("\tImportant: ", self.important)
        for t in self.tasks:
            t.print()


def load_json():
    i = 0
    try:
        with open('file.txt') as json_file:
            data = json.load(json_file)
            for p in data['projects']:
                project = Project(title=p['proj_name'],
                                     due_date=p['due_date'],
                                     description=p['description'],
                                     urgent=p['urgent'],
                                     important=p['important']
                                     )
                projects.append(project)
                for t in p['tasks']:
                    task = Task(title=t['task_name'],
                                   due_date=t['due_date'],
                                   description=t['description'],
                                   urgent=t['urgent'],
                                   important=t['important'],
                                   project=projects[i]
                                   )
                    projects[i].add_task(task)
                i = i + 1
    except:
        print("no projects")

def write_json():
    directory = {}
    task_directory = {}
    task_directory['tasks'] = []
    directory['projects'] = []
    for x in projects:
        for y in x.tasks:
            task_directory['tasks'].append({
                "task_name": y.title,
                "due_date": y.due_date,
                "description": y.description,
                "urgent": y.urgent,
                "important": y.important,
            })

        directory['projects'].append({
            "proj_name": x.title,
            "due_date": x.due_date,
            "description": x.description,
            "urgent": x.urgent,
            "important": x.important,
            "tasks": task_directory['tasks']
        })
        task_directory['tasks'] = []

    with open('file.txt', 'w') as outfile:
        json.dump(directory, outfile)

