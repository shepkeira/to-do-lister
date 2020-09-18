from tkinter import *
from global_functions import clear
import global_functions as gf
import proj_list_page
import main_page
from task_list_page import Task_List_Page
from calender_page import Calender_Page
from main_page import Main_Page
from task_page import Task_Page


class New_Task_Page:
    def __init__(self, content, proj, tasks):
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
        cancel_btn = Button(content, text="Cancel", command=lambda: Main_Page(content).grid(column=0, row=0))
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

        done_btn = Button(content, text="Done", command=lambda: (self.new_task(proj,
                                                                             task_name.get(),
                                                                             due_date.get(),
                                                                             description.get(),
                                                                             urgent.get(),
                                                                             important.get()
                                                                             ),
                                                                 proj_list_page.set_up(content)))
        done_btn.grid(column=1, row=6)

    def new_task(proj, name, date, desc, urg, imp):
        print("new task")
        urgent = False
        important = False
        if urg == 1:
            urgent = True
        if imp == 1:
            important = True
        new_task = gf.Task(title=name, due_date=date, description=desc, urgent=urgent, important=important, project=proj)
        proj.add_task(new_task)

        gf.write_json()
