import csv
from datetime import *
from tkinter import Tk, ttk
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter.ttk import Combobox
import time

from playsound import playsound


class Task:
    def __init__(self, name, sub, cat, description, link, loc, year, month, day, hour, minute, priority):
        self.description = description
        self.link = link
        self.loc = loc
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.priority = priority
        self.name = name
        self.cat = cat
        self.sub = sub

    def __str__(self):
        def snoze():
            screen.destroy()
            time.sleep(20)
            playsound("ring.mp3")
            return self

        def exit_s():
            screen.destroy()

        screen = Tk()
        screen.geometry("300x300")
        screen.title(self.name)
        Label(screen, text="Description :").grid(row=0, column=0, pady=10)
        Label(screen, text=self.description).grid(row=0, column=1)
        Label(screen, text="Link :").grid(row=1, column=0, pady=10)
        Label(screen, text=self.link).grid(row=1, column=1)
        Label(screen, text="location :").grid(row=2, column=0, pady=10)
        Label(screen, text=self.loc).grid(row=2, column=1)
        Label(screen, text="Subtask :").grid(row=3, column=0, pady=10)
        Label(screen, text=self.sub).grid(row=3, column=1)
        Button(screen, text="Snoze", command=snoze, width=15, bg="grey").grid(row=4, column=1, pady=20)
        Button(screen, text="Exit", command=exit_s, width=15, bg="grey").grid(row=4, column=0, pady=20)
        screen.mainloop()
        return "remind"

    def check(self):
        if self.priority == "":
            showinfo("notification", "Enter priority!")
            # logging.warning('No priority has been entered.')
            return False
        # CHECK FOR FILLING ALL BLANKS OF THE DATE
        if self.year == 0 \
                or self.month == 0 \
                or self.day == 0:
            showinfo("notification", "Enter date!")
            return False
        elif self.month == datetime.now().month:
            if self.day < datetime.now().day:
                showinfo("notification", "day pass")
                return False
            elif self.day == datetime.now().day:
                if self.hour < datetime.now().hour:
                    showinfo("notification", "hour pass")
                    return False
                elif self.hour == datetime.now().hour:
                    if self.minute < datetime.now().minute:
                        showinfo("notification", "minute pass")
                        return False
                    else:
                        return True
            # CHECK COMING YEARS
        else:
            return True
        # CHECK DAY OF MONTH
        if self.month == 2 and self.day > 29:
            showinfo("notification", "day is out of range for the month you choose")
            return False
        elif self.month == 4 \
                or self.month == 6 \
                or self.month == 9 \
                or self.month == 11:
            if self.day > 30:
                showinfo("notification", "day is out of range for the month you choose")
                return False
            else:
                return True
        # CHECK WHETHER INPUT DATE IS OVER
        elif self.year == datetime.now().year:
            if self.month < datetime.now().month:
                showinfo("notification", "month pass")
                return False

    # COMPARE INPUT DATE AND TIME WITH SYSTEM DATE AND TIME FOR REMINDING
    def remind(self):
        if self.year == datetime.now().year \
                and self.month == datetime.now().month \
                and self.day == datetime.now().day \
                and self.hour == datetime.now().hour \
                and self.minute == datetime.now().minute:
            return True
        return False

    def edit(self):
        def save():
            f = open(self.name + '.txt', 'w')
            f.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(subtask.get(), category.get(), descrip.get(),
                                                                        link.get(),
                                                                        location.get(),
                                                                        str(year.get()), str(month.get()),
                                                                        str(day.get()),
                                                                        str(hour.get()),
                                                                        str(minute.get()), priority.get()))
            f.close()
            showinfo("Info", "your task edit")
            # t.destroy()

        t = Tk()
        t.geometry("600x350")
        t.title(self.name)
        Label(t, text="Description :").grid(row=1, column=0, pady=10)
        descrip = Entry(t)
        descrip.grid(row=1, column=1, sticky=W)
        descrip.insert(END, self.description)
        Label(t, text="Link :").grid(row=2, column=0, pady=10)
        link = Entry(t)
        link.insert(0, self.link)
        link.grid(row=2, column=1, sticky=W)
        Label(t, text="location :").grid(row=3, column=0, pady=10)
        location = Entry(t)
        location.insert(0, self.loc)
        location.grid(row=3, column=1, sticky=W)
        Label(t, text="Priority :").grid(row=4, column=0, pady=10)
        priority = Combobox(t, values=["important", "normal"], state='readonly')
        priority.grid(row=4, column=1, sticky=W)
        priority.set(self.priority)
        Label(t, text="Date(y/m/d) :").grid(row=5, column=0, pady=10)
        year = ttk.Combobox(t,
                            values=list(range(2020, 2031)), state='readonly')
        year.grid(row=5, column=1, sticky=W)
        year.set(self.year)
        month = ttk.Combobox(t,
                             values=list(range(1, 13)),
                             state='readonly')

        month.grid(row=5, column=2, sticky=W)
        month.set(self.month)
        day = ttk.Combobox(t,
                           values=list(range(1, 32)),
                           state='readonly')
        day.grid(row=5, column=3, sticky=W)
        day.set(self.day)
        Label(t, text="Time(h:m) :").grid(row=6, column=0)
        hour = ttk.Combobox(t,
                            values=list(range(0, 24)),
                            state='readonly')
        hour.grid(row=6, column=1, pady=10, sticky=W)
        hour.set(self.hour)
        minute = ttk.Combobox(t,
                              values=list(range(0, 60)),
                              state='readonly')
        minute.grid(row=6, column=2, sticky=W)
        minute.set(self.minute)
        Label(t, text="Category").grid(row=7, column=0)
        category = ttk.Combobox(t, values=['maktab', 'uni', 'home'])
        category.grid(row=7, column=1)
        Label(t, text="Category").grid(row=7, column=0)
        category = ttk.Combobox(t, values=['maktab', 'uni', 'home'])
        category.grid(row=7, column=1)
        category.set(self.cat)
        Label(t, text="Subtask").grid(row=7, column=2, sticky=E)
        subtask = Entry(t)
        subtask.grid(row=7, column=3)
        subtask.insert(0, self.sub)
        Button(t, text="save", command=save).grid(row=8, column=3, pady=20, sticky=W)
        t.mainloop()

    def file_write(self):
        file_cat = open(self.cat + '.txt', 'a')
        file_cat.write(self.name)
        file_cat.close()
        f = open(self.name + '.txt', 'w')
        f.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(self.sub, self.cat, self.description, self.link,
                                                                    self.loc,
                                                                    str(self.year), str(self.month), str(self.day),
                                                                    str(self.hour),
                                                                    str(self.minute), self.priority))
        f.close()
        showinfo("notification", "reminder has been set")
