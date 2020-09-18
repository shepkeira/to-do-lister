from tkinter import *
import global_functions as gf
from global_functions import clear


class Proj_List_Page:
    def __init__(self, content):
        clear(content)
        from task_list_page import Task_List_Page
        from calender_page import Calender_Page
        from main_page import Main_Page
        menubar = Menu(content)
        menubar.add_command(label="Home", command=lambda: Main_Page(content))
        menubar.add_command(label="Projects", command=lambda: Proj_List_Page(content))
        menubar.add_command(label="Tasks", command=lambda: Task_List_Page(content))
        menubar.add_command(label="Calender", command=lambda: Calender_Page(content))
        content.config(menu=menubar)
        gf.load_json()

        print("proj list page")

        for x in gf.projects:
            x.print()

        project_labels = []
        i = 0
        for x in gf.projects:
            project_frame = Frame(content, highlightthickness=1, highlightbackground="black", bg=gf.dark_pink, width=15,
                                  height=5)

            project_frame.grid(column=0, row=i, padx=10, pady=10)
            title_label = Label(project_frame, text=x.title, bg=gf.dark_pink, width=15)
            title_label.grid(column=0, row=0)
            date_label = Label(project_frame, text=x.due_date, bg=gf.dark_pink, width=15)
            date_label.grid(column=0, row=1)
            from proj_page import Proj_Page
            proj_btn = Button(project_frame, text="View", bg=gf.grey_pink,
                              command=lambda i=i: Proj_Page(content, i).grid(column=0, row=0))
            proj_btn.grid(column=1, row=0, rowspan=2)
            project_labels.append(project_frame)
            i = i + 1

        from new_proj_page import New_Proj_Page
        new_proj_btn = Button(content, text="New Project", command=lambda: New_Proj_Page(content).grid(column=0, row=0), width=15,
                              height=2, bg=gf.light_blue)
        new_proj_btn.grid(column=0, row=i, padx=10, pady=10)