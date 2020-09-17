from tkinter import *
from global_functions import clear
import global_functions as gf
import proj_list_page
import task_list_page
import calender_page
import main_page
import json

def set_up(content, proj, tasks, projects):
    clear(content)
    print("new task page page")
    proj_title_label = Label(content, text="Project Name: ")
    proj_title_label.grid(column=0, row=0)
    proj_title_label = Label(content, text="Task Name: ")
    proj_title_label.grid(column=0, row=1)
    due_date_label = Label(content, text="Due Date and Time: ")
    due_date_label.grid(column=0, row=2)
    urgent_label = Label(content, text="Urgent: ")
    urgent_label.grid(column=0, row=3)
    important_label = Label(content, text="Important: ")
    important_label.grid(column=0, row=4)
    description_label = Label(content, text="Description: ")
    description_label.grid(column=0, row=5)
    cancel_btn = Button(content, text="Cancel", command=lambda: main_page.set_up(content))
    cancel_btn.grid(column=0, row=6)

    task_name = StringVar()
    due_date = StringVar()
    description = StringVar()
    urgent = IntVar()
    important = IntVar()

    proj_name_label = Label(content, text=proj.title)
    proj_name_label.grid(column=1, row=1)
    task_name_entry = Entry(content, textvariable=task_name)
    task_name_entry.grid(column=1, row=1)
    due_date_entry = Entry(content, textvariable=due_date)
    due_date_entry.grid(column=1, row=2)
    urgent_box = Checkbutton(content, textvariable=urgent)
    urgent_box.grid(column=1, row=3)
    important_box = Checkbutton(content, textvariable=important)
    important_box.grid(column=1, row=4)
    desc_entry = Entry(content, textvariable=description)
    desc_entry.grid(column=1, row=5)

    done_btn = Button(content, text="Done", command=lambda: (new_task(proj,
                                                                         projects,
                                                                         proj.title,
                                                                         task_name.get(),
                                                                         due_date.get(),
                                                                         description.get(),
                                                                         urgent.get(),
                                                                         important.get()
                                                                         ),
                                                             proj_list_page.set_up(content)))
    done_btn.grid(column=1, row=6)

def new_task(proj, projects, proj_name, name, date, desc, urg, imp):
    print("new task")
    urgent = False
    important = False
    if urg == 1:
        urgent = True
    if imp == 1:
        important = True
    new_task = gf.Task(title=name, due_date=date, description=desc, urgent=urgent, important=important, project=proj)
    proj.add_task(new_task)

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
            "tasks" : task_directory['tasks']
        })
        task_directory['tasks'] = []

    with open('file.txt', 'w') as outfile:
        json.dump(directory, outfile)
