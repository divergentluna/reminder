from datetime import *
from tkinter import Tk, ttk
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter.ttk import Combobox
import re
import csv

from playsound import playsound

import logging


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
        def snooze():
            screen.destroy()
            time.sleep(60)
            playsound("ring.mp3")
            logging.info(f'Reminder snoozed for 1 minute from {datetime.now()}')
            return self

        def exit_s():
            screen.destroy()

        screen = Tk()
        screen.geometry("200x200")
        screen.title(self.name)
        Label(screen, text="Description :").grid(row=0, column=0, pady=10)
        Label(screen, text=self.description).grid(row=0, column=1)
        Label(screen, text="Link :").grid(row=1, column=0, pady=10)
        Label(screen, text=self.link).grid(row=1, column=1)
        Label(screen, text="location :").grid(row=2, column=0, pady=10)
        Label(screen, text=self.loc).grid(row=2, column=1)
        Label(screen, text="Subtask :").grid(row=3, column=0, pady=10)
        Label(screen, text=self.sub).grid(row=3, column=1)
        Button(screen, text="Snoze", command=snooze, width=15, bg="grey").grid(row=4, column=1, pady=20)
        Button(screen, text="Exit", command=exit_s, width=15, bg="grey").grid(row=4, column=0, pady=20)
        screen.mainloop()
        return "remind"

    def check(self):
        # CHECK FOR FILLING ALL BLANKS OF THE DATE
        if self.year == 0 \
                or self.month == 0 \
                or self.day == 0:
            showinfo("notification", "Enter date!")
            logging.warning('No date has been entered.')
            return False
        # CHECK DAY OF MONTH
        elif self.month == 2:
            if self.day > 29:
                showinfo("notification", "day is out of range for the month you choose")
                logging.warning('Date out of range.')
                return False
            else:
                return True
        elif self.month == 4 \
                or self.month == 6 \
                or self.month == 9 \
                or self.month == 11:
            if self.day > 30:
                showinfo("notification", "day is out of range for the month you choose")
                logging.warning('Date/time out of range.')
                return False
            else:
                return True
        # CHECK WHETHER INPUT DATE IS OVER
        elif self.year == datetime.now().year:
            if self.month < datetime.now().month:
                showinfo("notification", "month pass")
                logging.warning('Date/time out of range.')
                return False
            elif self.month == datetime.now().month:
                if self.day < datetime.now().day:
                    showinfo("notification", "day pass")
                    logging.warning('Date/time out of range.')
                    return False
                elif self.day == datetime.now().day:
                    if self.hour < datetime.now().hour:
                        showinfo("notification", "hour pass")
                        logging.warning('Date/time out of range.')
                        return False
                    elif self.hour == datetime.now().hour:
                        if self.minute < datetime.now().minute:
                            showinfo("notification", "minute pass")
                            logging.warning('Date/time out of range.')
                            return False
                        else:
                            return True
        # CHECK COMING YEARS
        else:
            logging.info('Correct data has been entered')
            return True

        # CHECK IF URL IS IN CORRECT FORM
        if re.search("(?P<url>https?://[^\s]+)", self.link).group("url"):
            return True
        else:
            showinfo("notification", "URL is not correct!")
            logging.warning('Incorrect link entered.')
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
        t = Tk()
        t.geometry("600x350")
        t.title("REMINDER")
        Label(t, text="Name").grid(row=0)
        file_name = Entry(t)
        file_name.grid(row=0, column=1, pady=10)
        Label(t, text="Description :").grid(row=1, column=0, pady=10)

        descrip = Text(t, width=50, height=2, font=(("Arial"), 10), wrap=WORD)
        descrip.grid(row=1, column=1, columnspan=3, sticky=W)
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

        Label(t, text="Date(y/m/d) :").grid(row=5, column=0, pady=10)
        year = IntVar()
        ttk.Combobox(t, textvariable=year,
                     values=list(range(2020, 2031)), state='readonly').grid(row=5, column=1, sticky=W)

        month = IntVar()
        ttk.Combobox(t, textvariable=month,
                     values=list(range(1, 13)),
                     state='readonly').grid(row=5, column=2, sticky=W)
        month.set(self.month)
        day = IntVar()
        ttk.Combobox(t, textvariable=day,
                     values=list(range(1, 32)),
                     state='readonly').grid(row=5, column=3, sticky=W)
        day.set(self.day)
        Label(t, text="Time(h:m) :").grid(row=6, column=0)
        hour = IntVar()
        ttk.Combobox(t, textvariable=hour,
                     values=list(range(0, 24)),
                     state='readonly').grid(row=6, column=1, pady=10, sticky=W)
        hour.set(self.hour)
        minute = IntVar()
        ttk.Combobox(t, textvariable=minute,
                     values=list(range(0, 60)),
                     state='readonly').grid(row=6, column=2, sticky=W)
        minute.set(self.minute)
        Label(t, text="Category").grid(row=7, column=0)
        category = ttk.Combobox(t, values=['maktab', 'uni', 'home'])
        category.grid(row=7, column=1)

        set_button = Button(t, text="set").grid(row=8, column=3, pady=20, sticky=W)
        t.mainloop()

    def file_write(self):
        # TXT FILE SAVE FORM
        # file_cat = open(self.cat + '.txt', 'a')
        # file_cat.write(self.name)
        # file_cat.close()
        # f = open(self.name + '.txt', 'w')
        # f.write('{}\n{}\n{}\n{}\\{}\\{}\n{}:{}'.format(self.description, self.link, self.loc, str(self.year),
        #                                                str(self.month), str(self.day), str(self.hour),
        #                                                str(self.minute)))
        # f.close()
        # showinfo("notification", "reminder has been set")

        # CSV FILE SAVE FORM
        with open('alarms.csv', 'w', newline='') as csvfile:
            fieldnames = ['Name',
                          'Description', 'Link', 'Location',
                          'Category', 'SubTask', 'Priority',
                          'Year', 'Month', 'Day',
                          'Hour', 'Minute']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            writer.writerow({'Name': self.name, 'Description': self.description,
                             'Link': self.link, 'Location': self.loc,
                             'Category': self.cat, 'SubTask': self.sub, 'Priority': self.priority,
                             'Year': self.year, 'Month': self.month, 'Day': self.day,
                             'Hour': self.hour, 'Minute': self.minute})
            showinfo("notification", "reminder has been set")
            logging.info(
                f'New reminder set at {datetime.now()} for {self.year}/{self.month}/{self.day} at {self.hour}:{self.minute}')
