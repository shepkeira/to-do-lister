from tkinter import *
import global_functions as gf
from global_functions import clear


class Task_List_Page():
    def __init__(self, content):
        clear(content, bg=gf.grey_pink)
        from task_list_page import Task_List_Page
        from calender_page import Calender_Page
        from main_page import Main_Page
        from proj_list_page import Proj_List_Page
        menubar = Menu(content)
        menubar.add_command(label="Home", command=lambda: Main_Page(content))
        menubar.add_command(label="Projects", command=lambda: Proj_List_Page(content))
        menubar.add_command(label="Tasks", command=lambda: Task_List_Page(content))
        menubar.add_command(label="Calender", command=lambda: Calender_Page(content))
        content.config(menu=menubar)
        print("task list page")
        gf.load_json()

        task_labels = []
        i = 0
        for x in gf.projects:
            for y in x.tasks:
                task_frame = Frame(content, highlightthickness=1, highlightbackground="black", bg=gf.dark_pink,
                                   width=15,
                                   height=5)

                task_frame.grid(column=0, row=i, padx=10, pady=10)
                title_label = Label(task_frame, text=x.title + ": " + y.title, bg=gf.dark_pink, width=15)
                title_label.grid(column=0, row=0)
                date_label = Label(task_frame, text=y.due_date, bg=gf.dark_pink, width=15)
                date_label.grid(column=0, row=1)
                from task_page import Task_Page
                proj_btn = Button(task_frame, text="View", bg=gf.grey_pink,
                                  command=lambda y=y, proj=x: Task_Page(content, y, proj).grid(column=0, row=0))
                proj_btn.grid(column=1, row=0, rowspan=2)
                task_labels.append(task_frame)
                i = i + 1