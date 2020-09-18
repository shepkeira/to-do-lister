from tkinter import *
import global_functions as gf
from global_functions import clear


class Proj_Page:
    def __init__(self, content, index):
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
        proj = gf.projects[index]

        Proj_Name_Label = Label(content, text=proj.title, bg=gf.light_pink)
        Proj_Name_Label.grid(column=0, row=0)
        Proj_Date_Label = Label(content, text=proj.due_date, bg=gf.light_pink)
        Proj_Date_Label.grid(column=0, row=1)
        urgent_text = "Urgent: "
        important_text = "Important: "
        if proj.urgent:
            urgent_text = urgent_text + "Yes"
        else:
            urgent_text = urgent_text + "No"
        if proj.important:
            important_text = important_text + "Yes"
        else:
            important_text = important_text + "No"
        Proj_U_Label = Label(content, text=urgent_text, bg=gf.light_pink)
        Proj_U_Label.grid(column=1, row=0)
        Proj_I_Label = Label(content, text=important_text, bg=gf.light_pink)
        Proj_I_Label.grid(column=1, row=1)

        task_labels = []
        i = 2
        for y in proj.tasks:
            task_frame = Frame(content, highlightthickness=1, highlightbackground="black", bg=gf.dark_pink, width=15,
                               height=5)

            task_frame.grid(column=0, row=i, padx=10, pady=10)
            title_label = Label(task_frame, text=y.title, bg=gf.dark_pink, width=15)
            title_label.grid(column=0, row=0)
            date_label = Label(task_frame, text=y.due_date, bg=gf.dark_pink, width=15)
            date_label.grid(column=0, row=1)
            from task_page import Task_Page
            proj_btn = Button(task_frame, text="View", bg=gf.grey_pink, command=lambda y=y, proj=proj: Task_Page(content, y, proj))
            proj_btn.grid(column=1, row=0, rowspan=2)
            task_labels.append(task_frame)
            i = i + 1

        from new_task_page import New_Task_Page
        New_Task_Btn = Button(content, text="New Task", command=lambda: New_Task_Page(content, proj, proj.tasks), bg=gf.light_blue)
        New_Task_Btn.grid(column=0, row=i)
        print("proj list page")
