from tkinter import *
import global_functions as gf
from global_functions import clear


class Main_Page:
    def __init__(self, content):
        clear(content)
        from proj_list_page import Proj_List_Page
        from task_list_page import Task_List_Page
        from calender_page import Calender_Page
        menubar = Menu(content)
        menubar.add_command(label="Home", command=lambda: Main_Page(content))
        menubar.add_command(label="Projects", command=lambda: Proj_List_Page(content))
        menubar.add_command(label="Tasks", command=lambda: Task_List_Page(content))
        menubar.add_command(label="Calender", command=lambda: Calender_Page(content))
        content.config(menu=menubar)
        content.config(bg=gf.light_pink)
        proj_button = Button(content, text="Projects", command=lambda: (Proj_List_Page(content).grid(column=0, row=0)), width=15,
                             height=5, bg=gf.dark_pink)
        task_button = Button(content, text="Tasks", command=lambda: (Task_List_Page(content).grid(column=0, row=0)), width=15,
                             height=5, bg=gf.dark_pink)
        calender_button = Button(content, text="Calender", command=lambda: (Calender_Page(content).grid(column=0, row=0)), width=15,
                                 height=5, bg=gf.dark_pink)
        reset_button = Button(content, text="Reset", command=gf.reset, width=15, height=5, bg=gf.dark_pink)
        proj_button.grid(column=0, row=0, padx=10, pady=10)
        task_button.grid(column=1, row=0, padx=10, pady=10)
        calender_button.grid(column=0, row=1, padx=10, pady=10)
        reset_button.grid(column=1, row=1, padx=10, pady=10)
