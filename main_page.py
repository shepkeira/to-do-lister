from tkinter import *
import global_functions as gf
from global_functions import clear
import proj_list_page
import task_list_page
import calender_page


def set_up(content):
    clear(content)
    content.config(bg=gf.light_pink)
    #content.Style.configure(background="#DBCBD8")
    proj_button = Button(content, text="Projects", command=lambda: (proj_list_page.set_up(content)), width=15, height=5, bg=gf.dark_pink)
    task_button = Button(content, text="Tasks", command=lambda: (task_list_page.set_up(content)), width=15, height=5, bg=gf.dark_pink)
    calender_button = Button(content, text="Calender", command=lambda: (calender_page.set_up(content)), width=15, height=5, bg=gf.dark_pink)
    reset_button = Button(content, text="Reset", command=reset, width=15, height=5, bg=gf.dark_pink)
    proj_button.grid(column=0, row=0, padx=10, pady=10)
    task_button.grid(column=1, row=0, padx=10, pady=10)
    calender_button.grid(column=0, row=1, padx=10, pady=10)
    reset_button.grid(column=1, row=1, padx=10, pady=10)


def reset():
    print("reset")
    #delete everything from .txt doc