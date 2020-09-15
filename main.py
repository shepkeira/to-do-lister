from tkinter import *
from tkinter import ttk
import main_page


def set_up():
    root = Tk()
    root.wm_title("Herding Cats")
    return root


def start(root, content):
    main_page.set_up(content)
    root.mainloop()


root = set_up()
content = Frame(root)
content.grid(column=0, row=0)

start(root, content)