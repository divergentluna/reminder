from tkinter import ttk

from playsound import *
from datetime import datetime
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *

t = Tk()
t.geometry("600x300")


def check():
    if year.get() == 0 \
            or month.get() == 0 \
            or day.get() == 0 \
            or hour_user.get() == 0:
        showinfo("notification", "Enter date and time!!")
    else:
        remind()


def remind():
    showinfo("notification", "reminder has been set")

    if year.get() == datetime.now().year \
            and month.get() == datetime.now().month \
            and day.get() == datetime.now().day \
            and hour_user.get() == datetime.now().hour \
            and minute_user.get() == datetime.now().minute:
        # playsound("ring.mp3")
        screen = Tk()
        Label(screen, text="Description :").grid(row=0, column=0, pady=10)
        Label(screen, text=descrip.get(1.0, END)).grid(row=0, column=1)
        Label(screen, text="Link :").grid(row=1, column=0, pady=10)
        Label(screen, text=link.get()).grid(row=1, column=1)
        Label(screen, text="location :").grid(row=2, column=0, pady=10)
        Label(screen, text=location.get()).grid(row=2, column=1)
        screen.mainloop()


t.title("REMINDER")
Label(t, text="Description :").grid(row=0, column=0, pady=10)

descrip = Text(t, width=50, height=2, font=(("Arial"), 10), wrap=WORD)
descrip.grid(row=0, column=1, columnspan=3, sticky=W)

Label(t, text="Link :").grid(row=1, column=0, pady=10)
link = Entry(t)
link.grid(row=1, column=1, sticky=W)

Label(t, text="location :").grid(row=2, column=0, pady=10)
location = Entry(t)
location.grid(row=2, column=1, sticky=W)

Label(t, text="Priority :").grid(row=3, column=0, pady=10)
priority = Combobox(t, values=["important", "normal"], state='readonly').grid(row=3, column=1, sticky=W)

Label(t, text="Date(y/m/d) :").grid(row=4, column=0, pady=10)
year = IntVar()
ttk.Combobox(t, textvariable=year,
             values=list(range(2020, 2031)),
             state='readonly').grid(row=4, column=1, sticky=W)
month = IntVar()
ttk.Combobox(t, textvariable=month,
             values=list(range(1, 13)),
             state='readonly').grid(row=4, column=2, sticky=W)
day = IntVar()
ttk.Combobox(t, textvariable=day,
             values=list(range(1, 32)),
             state='readonly').grid(row=4, column=3, sticky=W)

Label(t, text="Time(h:m) :").grid(row=5, column=0)
hour_user = IntVar()
ttk.Combobox(t, textvariable=hour_user,
             values=list(range(1, 25)),
             state='readonly').grid(row=5, column=1, sticky=W)
minute_user = IntVar()
ttk.Combobox(t, textvariable=minute_user,
             values=list(range(0, 60)),
             state='readonly').grid(row=5, column=2, sticky=W)

b_1 = Button(t, text="set", command=check).grid(row=6, column=2, pady=20)

t.mainloop()

