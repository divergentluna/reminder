import os
from tkinter.ttk import *
from task import *
import logging

# for creating a log file
logging.basicConfig(filename='reminder_log.log', level=logging.INFO)
list_task = list()


def new():
    logging.info(f'Programme closed at {datetime.now()}')
    screen_1.destroy()

    def main():
        li = link.get()
        loc = location.get()
        des = descrip.get()
        y = year.get()
        m = month.get()
        d = day.get()
        h = hour.get()
        min = minute.get()
        p = priority.get()
        file = file_name.get()
        cat = category.get()
        sub = subtask.get()
        obj_task = Task(file, sub, cat, des, li, loc, y, m, d, h, min, p)

        # check if the object and values of task is in file or not
        if obj_task.check():
            if file not in list_task:
                obj_task.file_write()
                list_task.append(file)
            else:
                showinfo("Error", "name is available")
                logging.error('Name already exists')

    # new reminder set page display
    t2 = Tk()
    t2.geometry("600x350")
    t2.title("REMINDER")
    Label(t2, text="Name").grid(row=0)
    file_name = Entry(t2)
    file_name.grid(row=0, column=1, pady=10)
    Label(t2, text="Description :").grid(row=1, column=0, pady=10)

    descrip = Entry(t2)
    descrip.grid(row=1, column=1, sticky=W)

    Label(t2, text="Link :").grid(row=2, column=0, pady=10)
    link = Entry(t2)
    link.grid(row=2, column=1, sticky=W)

    Label(t2, text="location :").grid(row=3, column=0, pady=10)
    location = Entry(t2)
    location.grid(row=3, column=1, sticky=W)

    Label(t2, text="Priority :").grid(row=4, column=0, pady=10)
    priority = Combobox(t2, values=["important", "normal"], state='readonly')
    priority.grid(row=4, column=1, sticky=W)

    Label(t2, text="Date(y/m/d) :").grid(row=5, column=0, pady=10)
    year = IntVar()
    ttk.Combobox(t2, textvariable=year,
                 values=list(range(2020, 2031)),
                 state='readonly').grid(row=5, column=1, sticky=W)
    month = IntVar()
    ttk.Combobox(t2, textvariable=month,
                 values=list(range(1, 13)),
                 state='readonly').grid(row=5, column=2, sticky=W)
    day = IntVar()
    ttk.Combobox(t2, textvariable=day,
                 values=list(range(1, 32)),
                 state='readonly').grid(row=5, column=3, sticky=W)

    Label(t2, text="Time(h:m) :").grid(row=6, column=0)
    hour = IntVar()
    ttk.Combobox(t2, textvariable=hour,
                 values=list(range(0, 24)),
                 state='readonly').grid(row=6, column=1, pady=10, sticky=W)
    minute = IntVar()
    ttk.Combobox(t2, textvariable=minute,
                 values=list(range(0, 60)),
                 state='readonly').grid(row=6, column=2, sticky=W)
    Label(t2, text="Category").grid(row=7, column=0)
    category = ttk.Combobox(t2, values=['maktab', 'uni', 'home'])
    category.grid(row=7, column=1)
    Label(t2, text="Subtask").grid(row=7, column=2, sticky=E)
    subtask = Entry(t2)
    subtask.grid(row=7, column=3)
    Button(t2, text="set", command=main, width=15, bg="grey").grid(row=8, column=1, pady=20)
    t2.mainloop()


# close the menu screen
def exit_m():
    logging.info(f'Main menu closed at {datetime.now()}')
    screen_1.destroy()


# read each line of file and write it into a list
# to use it as details of reminder
def edit():
    try:
        file = name_file.get()
        f = open(file + '.txt')
        list = f.readlines()
        sub = str(list[0]).rstrip('\n')
        cat = str(list[1]).rstrip('\n')
        des = str(list[2]).rstrip('\n')
        li = str(list[3]).rstrip('\n')
        loc = str(list[4]).rstrip('\n')
        y = str(list[5]).rstrip('\n')
        m = str(list[6]).rstrip('\n')
        d = str(list[7]).rstrip('\n')
        h = str(list[8]).rstrip('\n')
        min = str(list[9]).rstrip('\n')
        p = str(list[10]).rstrip('\n')
        f.close()
        obj_edit = Task(file, sub, cat, des, li, loc, y, m, d, h, min, p)
        obj_edit.edit()

    # exception
    except FileNotFoundError:
        showinfo("Error", "please,enter correct file!!")
        logging.error('Not a correct file for read.')


# remove the file of reminder
def remove():
    try:
        file_name = name_file.get()
        os.remove(file_name + '.txt')
        showinfo("Info", "your task delete")
        logging.warning(f'One task has been removed.')
    except Exception:
        showinfo("Error", "please,enter correct file!!")
        logging.error('Not a correct file for read.')


# menu screen
screen_1 = Tk()
screen_1.title("Menu")
Label(text="name of task").grid(row=0, column=0)
name_file = Entry(screen_1)
name_file.grid(row=0, column=1)
edit_button = Button(screen_1, text="edit", command=edit, width=15, bg="grey").grid(row=2, column=2)
remove_button = Button(screen_1, text="remove", width=15, command=remove, bg="grey").grid(row=2, column=3)
new_button = Button(screen_1, text="new", command=new, width=15, bg="grey").grid(row=3, column=2, pady=10)
exit_button = Button(screen_1, text="exit", command=exit_m, width=15, bg="grey").grid(row=3, column=3, padx=10)
screen_1.mainloop()

# read each line of file and write it into a list
# to use it as details of reminder
for name in list_task:
    f = open(name + '.txt')
    list = f.readlines()
    sub = str(list[0]).rstrip('\n')
    cat = str(list[1]).rstrip('\n')
    des = str(list[2]).rstrip('\n')
    li = str(list[3]).rstrip('\n')
    loc = str(list[4]).rstrip('\n')
    y = str(list[5]).rstrip('\n')
    m = str(list[6]).rstrip('\n')
    d = str(list[7]).rstrip('\n')
    h = str(list[8]).rstrip('\n')
    min = str(list[9]).rstrip('\n')
    p = str(list[10]).rstrip('\n')
    f.close()
    obj_task_2 = Task(name, sub, cat, des, li, loc, int(y), int(m), int(d), int(h), int(min), p)

    # play sound for normal priority once
    flag = True
    if p == 'normal':
        while flag:
            if obj_task_2.remind():
                playsound("ring.mp3")
                logging.info('Alarm ringed!')
                print(obj_task_2)
                flag = False
    else:  # play sound for important priority once again after some seconds
        if obj_task_2.remind():
            playsound("ring.mp3")
            logging.info('Alarm ringed!')
            print(obj_task_2)
            time.sleep(6)
            playsound("ring.mp3")
            logging.info('Alarm ringed!')
            print(obj_task_2)
            flag = False
