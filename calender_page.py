from tkinter import *
from global_functions import clear
import tkcalendar as cal
import global_functions as gf
import time
import datetime
import tkinter.scrolledtext as scrolledtext


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
        gf.load_json()

        today = datetime.date.today()
        mindate = datetime.date(year=2000, month=1, day=1)
        maxdate = today + datetime.timedelta(days=365)
        CALENDAR = cal.Calendar(content,
                                background= gf.light_pink,
                                foreground= gf.dark_pink,
                                headersbackground = gf.dark_pink,
                                headersforeground = gf.light_pink,
                                selectforeground = 'white',
                                selectbackground = gf.dark_blue,
                                normalbackground = gf.light_pink,
                                normalforeground= gf.dark_pink,
                                weekendbackground=gf.light_pink,
                                weekendforeground=gf.dark_pink,
                                othermonthbackground=gf.grey_pink,
                                othermonthforeground=gf.light_pink,
                                othermonthwebackground=gf.grey_pink,
                                othermonthweforeground=gf.light_pink,
                                font="Arial 14",
                                selectmode='day',
                                locale='en_US',
                                mindate=mindate,
                                maxdate=maxdate,
                                disabledforeground='red',
                                cursor="hand1",
                                date_pattern='dd/mm/yyyy',
                                year=int(time.strftime('%Y')),
                                month=int(time.strftime('%m')),
                                day=int(time.strftime('%d')))
        CALENDAR.pack(fill="both", expand=True)

        # textbox
        text_box = scrolledtext.ScrolledText(content, width=10, height=10, wrap='word')
        text_box.pack(fill="x", expand=True)

        # highlight date
        def set_project(date_gotten, title):
            #print(date_gotten)
            date = datetime.date(day=int(date_gotten[:2]),
                                 month=int(date_gotten[3:5]),
                                 year=int(date_gotten[6:10])
                                 )
            #text_box.insert(END, '\n' + str(date_gotten) + ' - ')
            CALENDAR.calevent_create(date, title, 'project')
            CALENDAR.tag_config('project', background=gf.light_blue, foreground='white')

        def set_task(date_gotten, title):
            #print(date_gotten)
            date = datetime.date(day=int(date_gotten[:2]),
                                 month=int(date_gotten[3:5]),
                                 year=int(date_gotten[6:10])
                                 )
            #text_box.insert(END, '\n' + str(date_gotten) + ' - ')
            CALENDAR.calevent_create(date, title, 'task')
            CALENDAR.tag_config('task', background=gf.dark_pink, foreground='white')

        for x in gf.projects:
            set_project(x.due_date[:10], x.title)
            for y in x.tasks:
                set_task(y.due_date[:10], y.title)

        # un-highlight date
        def delete_event():
            date_gotten = CALENDAR.selection_get()
            CALENDAR.tag_config(date_gotten, background='blue', foreground='white')

        # save text
        def save():
            t = text_box.get(0.0, END)
            to_save = open('TEXT FILE', 'w')
            to_save.write(t)
            to_save.close()


        # load text
        #def load():
        #    to_load = open('TEXT FILE', 'r').read()
        #    text_box.delete(0.0, END)
        #    text_box.insert(0.0, to_load)

        # sets time as window title
        def time_set():
            content.title(time.strftime('%c'))
            content.after(10, time_set)

        def print_events(var):
            text_box.delete('1.0', END)
            date = CALENDAR.get_date()
            for x in gf.projects:
                if date in x.due_date:
                    text_box.insert(END, '\n' + str(x.due_date) + ' - ' + x.title)
                for y in x.tasks:
                    if date in y.due_date:
                        text_box.insert(END, '\n' + str(y.due_date) + ' - ' + y.title)

        content.bind("<<CalendarSelected>>", print_events)
        # buttons
        # confirm = Button(content, text='Create Event', command=set_event)
        # confirm.pack(fill="x", expand=True)
        # delete = Button(content, text='Delete Event', command=delete_event)
        # delete.pack(fill="x", expand=True)
        # save_ = Button(content, text='Save', command=save)
        # save_.pack(fill="x", expand=True)
        # load_ = Button(content, text='Load', command=load)
        # load_.pack(fill="x", expand=True)
        time_set()



