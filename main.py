from tkinter import ttk

from playsound import *
from datetime import datetime
from tkinter import *

from tkinter.ttk import *
from task import *

import logging

logging.basicConfig(filename='reminder_log.log', level=logging.INFO)


def new():
    logging.info(f'Programme closed at {datetime.now()}')
    t.destroy()

    def edit():
        li = link.get()
        loc = location.get()
        des = descrip.get(1.0, END)
        y = year.get()
        m = month.get()
        d = day.get()
        h = hour.get()
        min = minute.get()
        p = priority.get()
        file = file_name.get()
        cat = category.get()
        sub = subtask.get()
        obj_task = Task(file, sub, cat, des, li, loc, y, m, d, h, min)
        obj_task.edit()

    def main():
        li = link.get()
        loc = location.get()
        des = descrip.get(1.0, END)
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

        if obj_task.check():
            obj_task.file_write()
            flag = True
            while flag:
                #t2.destroy()
                if obj_task.remind():
                    playsound("ring.mp3")
                    flag = False
                    print(obj_task)

    t2 = Tk()
    t2.geometry("600x350")
    t2.title("REMINDER")
    Label(t2, text="Name").grid(row=0)
    file_name = Entry(t2)
    file_name.grid(row=0, column=1, pady=10)
    Label(t2, text="Description :").grid(row=1, column=0, pady=10)

    descrip = Text(t2, width=50, height=2, font=("Arial", 10), wrap=WORD)
    descrip.grid(row=1, column=1, columnspan=3, sticky=W)

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
    Label(text="Subtask").grid(row=7, column=2, sticky=E)
    subtask = Entry(t2)
    subtask.grid(row=7, column=3)
    Button(t2, text="set", command=main, width=15, bg="grey").grid(row=8, column=1, pady=20)
    t2.mainloop()


def exit_m():
    t.destroy()


def edit():
    import tkinter as tk
    from tkinter.filedialog import askopenfilename, asksaveasfilename

    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Simple Text Editor - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"Simple Text Editor - {filepath}")

    window = tk.Tk()
    window.title("Simple Text Editor")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()


def remove():
    # name_file.get open and delete
    showinfo("notifacation", "your task delete")
    pass


t = Tk()
t.title("Menu")
Label(text="name of task").grid(row=0, column=0)
name_file = Entry(t)
name_file.grid(row=0, column=1)
edit_button = Button(t, text="edit", command=edit, width=15, bg="grey").grid(row=2, column=2)
remove_button = Button(t, text="remove", width=15, command=remove, bg="grey").grid(row=2, column=3)
new_button = Button(t, text="new", command=new, width=15, bg="grey").grid(row=3, column=2, pady=10)
exit_button = Button(t, text="exit", command=exit_m, width=15, bg="grey").grid(row=3, column=3, padx=10)
t.mainloop()
