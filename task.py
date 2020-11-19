from datetime import datetime
from datetime import timedelta
from tkinter.messagebox import showinfo


class Task:
    def __init__(self, description, link, loc, year, month, day, hour, minute, priority):
        self.description = description
        self.link = link
        self.loc = loc
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.priority = priority
    #COMPARE INPUT DATE AND TIME WITH SYSTEM DATE AND TIME FOR REMINDING
    def remind(self):
        if self.year == datetime.now().year \
                and self.month == datetime.now().month \
                and self.day == datetime.now().day \
                and self.hour == datetime.now().hour \
                and self.minute == datetime.now().minute:
            return True
        return False






class Check:
    def __init__(self, year, month, day, hour, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def check(self):
        #CHECK FOR FILLING ALL BLANKS OF THE DATE
        if self.year == 0 \
                or self.month == 0 \
                or self.day == 0:
            showinfo("notification", "Enter date!")
            return False
        # CHECK DAY OF MONTH
        elif self.month == 2:
            if self.day > 29:
                showinfo("notification", "day is out of range for the month you choose")
        elif self.month == 4 \
                or self.month == 6 \
                or self.month == 9 \
                or self.month == 11 :
            if self.day > 30:
                showinfo("notification", "day is out of range for the month you choose")
        #CHECK WHETHER INPUT DATE IS OVER
        elif self.year == datetime.now().year:
            if self.month < datetime.now().month:
                showinfo("notification", "month pass")
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
        #CHECK COMING YEARS
        else:
            return True


