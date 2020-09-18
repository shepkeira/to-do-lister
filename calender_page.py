from tkinter import *
from global_functions import clear
import global_functions as gf


class Calender_Page:
    def __init__(self, content):
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
        print("calender page")
        # TODO 6: create calender page

