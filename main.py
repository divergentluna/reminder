from tkinter import ttk

from playsound import *
from datetime import datetime
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *


def check():
    if year.get() == 0 \
            or month.get() == 0 \
            or day.get() == 0 :
        showinfo("notification", "Enter date and time!!")
    else:
        li = link.get()
        loc = location.get()
        des = descrip.get(1.0, END)
        y = year.get()
        m = month.get()
        d = day.get()
        h = hour_user.get()
        min = minute_user.get()

        f = open('1.txt', 'w')
        f.write('{}\n{}\n{}\n{}\\{}\\{}\n{}:{}'.format(des, li, loc, str(y), str(m), str(d), str(h), str(min)))

        showinfo("notification", "reminder has been set")
        # t.destroy()
        status = True
        while status == True:
            f = open('1.txt')
            lines = f.readlines()
            des = lines[0]
            li = lines[2]
            loc = lines[3]
            date = lines[4].split('\\')
            time = lines[5].split(':')
            if 0 <= int(time[1]) < 10 or 0 <= int(time[0]) < 10 or 0 <= int(date[1]) < 10 or 0 <= int(date[2]) < 10:
                time[1] = '0' + time[1]
                time[0] = '0' + time[0]
                date[1] = '0' + date[1]
                date[2] = '0' + date[2]
            if int(date[0]) == datetime.now().year \
                    and int(date[1]) == datetime.now().month \
                    and int(date[2].rstrip('\n')) == datetime.now().day \
                    and int(time[0]) == datetime.now().hour \
                    and int(time[1]) == datetime.now().minute:
                status=False
                screen = Tk()
                Label(screen, text="Description :").grid(row=0, column=0, pady=10)
                Label(screen, text=des).grid(row=0, column=1)
                Label(screen, text="Link :").grid(row=1, column=0, pady=10)
                Label(screen, text=li).grid(row=1, column=1)
                Label(screen, text="location :").grid(row=2, column=0, pady=10)
                Label(screen, text=loc).grid(row=2, column=1)
                playsound("ring.mp3")

                screen.mainloop()


t = Tk()
t.geometry("600x300")
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
             values=list(range(0, 24)),
             state='readonly').grid(row=5, column=1, sticky=W)
minute_user = IntVar()
ttk.Combobox(t, textvariable=minute_user,
             values=list(range(0, 60)),
             state='readonly').grid(row=5, column=2, sticky=W)
set_button = Button(t, text="set", command=check).grid(row=6, column=3, pady=20)
# save_button = Button(t, text="save", command=save).grid(row=6, column=2, pady=20)
t.mainloop()
