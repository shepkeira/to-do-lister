from tkinter import *
#TODO add clear content

def set_up():
    root = Tk()
    root.wm_title("Herding Cats")
    return root


def menubar(root):
    menubar = Menu(root)
    pageMenu = Menu(menubar)
    pageMenu.add_command(label="Home")
    menubar.add_cascade(label="Home", menu=pageMenu)
    return menubar


def start(content):
    from main_page import Main_Page
    Main_Page(content)#.grid(column=0, row=0)
    content.mainloop()


#root = set_up()
content = set_up()
#content.grid(column=0, row=0)

start(content)