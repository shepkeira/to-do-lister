from tkinter import *
import global_functions as gf
import proj_list_page
from main_page import Main_Page
from task_list_page import Task_List_Page
from calender_page import Calender_Page
from main_page import Main_Page
from task_page import Task_Page
from global_functions import clear


class New_Proj_Page:
    def __init__(self, content):
        clear(content)
        proj_title_label = Label(content, text="Project Name: ")
        proj_title_label.grid(column=0, row=0)
        due_date_label = Label(content, text="Due Date and Time (dd/mm/yy 24:00): ")
        due_date_label.grid(column=0, row=1)
        urgent_label = Label(content, text="Urgent: ")
        urgent_label.grid(column=0, row=2)
        important_label = Label(content, text="Important: ")
        important_label.grid(column=0, row=3)
        description_label = Label(content, text="Description: ")
        description_label.grid(column=0, row=4)
        cancel_btn = Button(content, text="Cancel", command=lambda: Main_Page(content))
        cancel_btn.grid(column=0, row=5)

        proj_name = StringVar()
        due_date = StringVar()
        description = StringVar()
        urgent = IntVar()
        important = IntVar()

        proj_name_entry = Entry(content, textvariable=proj_name)
        proj_name_entry.grid(column=1, row=0)
        due_date_entry = Entry(content, textvariable=due_date)
        due_date_entry.grid(column=1, row=1)
        urgent_box = Checkbutton(content, textvariable=urgent)
        urgent_box.grid(column=1, row=2)
        important_box = Checkbutton(content, textvariable=important)
        important_box.grid(column=1, row=3)
        desc_entry = Entry(content, textvariable=description)
        desc_entry.grid(column=1, row=4)

        done_btn = Button(content, text="Done", command=lambda: (self.new_project(proj_name.get(),
                                                                             due_date.get(),
                                                                             description.get(),
                                                                             urgent.get(),
                                                                             important.get()
                                                                             ),
                                                                 proj_list_page.set_up(content)))
        done_btn.grid(column=1, row=5)

    def new_project(name, date, desc, urg, imp):
        print("new proj")
        urgent = False
        important = False
        if urg == 1:
            urgent = True
        if imp == 1:
            important = True
        new_proj = gf.Project(name, date, desc, urgent, important)
        gf.projects.append(new_proj)
        gf.write_json()
