light_pink = "#EABFCB"
grey_pink = "#C191A1"
dark_pink = "#A4508B"
light_blue = "#5F0A87"
dark_blue = "#2F004F"

def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()


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
        self.due_date = due_date #TODO 5 make into date format to use later
        self.description = description
        self.urgent = urgent
        self.important = important
        self.tasks = tasks

    def __init__(self, title, due_date, description, urgent, important):
        self.title = title
        self.due_date = due_date #TODO 4 make into date format to use later
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
