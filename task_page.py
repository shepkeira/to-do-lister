from tkinter import *
import global_functions as gf
from global_functions import clear

class Task_Page:
    def __init__(self, content, task, project):
        clear(content)
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
        print("task page")

        Proj_Name_Label = Label(content, text=project.title, bg=gf.light_pink)
        Proj_Name_Label.grid(column=0, row=0)
        Task_Name_Label = Label(content, text=task.title, bg=gf.light_pink)
        Task_Name_Label.grid(column=0, row=1)
        Task_Date_Label = Label(content, text=task.due_date, bg=gf.light_pink)
        Task_Date_Label.grid(column=0, row=2)
        Task_Desc_Label = Label(content, text=task.description, bg=gf.light_pink)
        Task_Desc_Label.grid(column=0, row=3, columnspan=2)
        urgent_text = "Urgent: "
        important_text = "Important: "
        if task.urgent:
            urgent_text = urgent_text + "Yes"
        else:
            urgent_text = urgent_text + "No"
        if task.important:
            important_text = important_text + "Yes"
        else:
            important_text = important_text + "No"
        Task_U_Label = Label(content, text=urgent_text, bg=gf.light_pink)
        Task_U_Label.grid(column=1, row=0)
        Task_I_Label = Label(content, text=important_text, bg=gf.light_pink)
        Task_I_Label.grid(column=1, row=1)


