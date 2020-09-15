from tkinter import *
import global_functions as gf
from global_functions import clear
import proj_list_page
import task_list_page
import calender_page
import main_page
import new_task_page
import task_page
import json

def set_up(content):
    clear(content)
    projects = []
    i = 0
    with open('file.txt') as json_file:
        data = json.load(json_file)
        for p in data['projects']:
            project = gf.Project(title=p['proj_name'],
                                 due_date=p['due_date'],
                                 description=p['description'],
                                 urgent=p['urgent'],
                                 important=p['important']
                                 )
            projects.append(project)
            for t in p['tasks']:
                task = gf.Task(title=t['task_name'],
                               due_date=t['due_date'],
                               description=t['description'],
                               urgent=t['urgent'],
                               important=t['important'],
                               project=projects[i]
                               )
                projects[i].add_task(task)
            i = i + 1

    print("proj list page")

    for x in projects:
        x.print()

    task_labels = []
    i = 0
    for x in projects:
        for y in x.tasks:
            task_frame = Frame(content, highlightthickness=1, highlightbackground="black", bg=gf.dark_pink, width=15,
                               height=5)

            task_frame.grid(column=0, row=i, padx=10, pady=10)
            title_label = Label(task_frame, text=x.title + ": " + y.title, bg=gf.dark_pink, width=15)
            title_label.grid(column=0, row=0)
            date_label = Label(task_frame, text=y.due_date, bg=gf.dark_pink, width=15)
            date_label.grid(column=0, row=1)
            proj_btn = Button(task_frame, text="View", bg=gf.grey_pink, command=lambda: task_page.set_up(content, y, x))
            proj_btn.grid(column=1, row=0, rowspan=2)
            task_labels.append(task_frame)
            i = i + 1