from tkinter import ttk

from playsound import *
from datetime import datetime
from tkinter import *

from tkinter.ttk import *
from task import *

def new():
    exit()
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
        obj_check = Check(y, m, d, h, min)
        if obj_check.check():
            file_cat = open(cat + '.txt', 'a')
            file_cat.write(file)
            file_cat.close()
            f = open(file + '.txt', 'w')
            f.write('{}\n{}\n{}\n{}\\{}\\{}\n{}:{}'.format(des, li, loc, str(y), str(m), str(d), str(h), str(min)))
            f.close()
            showinfo("notification", "reminder has been set")
            obj_task = Task(des, li, loc, y, m, d, h, min)
            flag = True
            while flag == True:
                if obj_task.remind():
                    screen = Tk()
                    Label(screen, text="Description :").grid(row=0, column=0, pady=10)
                    Label(screen, text=des).grid(row=0, column=1)
                    Label(screen, text="Link :").grid(row=1, column=0, pady=10)
                    Label(screen, text=li).grid(row=1, column=1)
                    Label(screen, text="location :").grid(row=2, column=0, pady=10)
                    Label(screen, text=loc).grid(row=2, column=1)
                    playsound("ring.mp3")
                    flag = False
                    screen.mainloop()

    t = Tk()
    t.geometry("600x350")
    t.title("REMINDER")
    Label(t, text="Name").grid(row=0)
    file_name = Entry(t)
    file_name.grid(row=0, column=1, pady=10)
    Label(t, text="Description :").grid(row=1, column=0, pady=10)

    descrip = Text(t, width=50, height=2, font=(("Arial"), 10), wrap=WORD)
    descrip.grid(row=1, column=1, columnspan=3, sticky=W)

    Label(t, text="Link :").grid(row=2, column=0, pady=10)
    link = Entry(t)
    link.grid(row=2, column=1, sticky=W)

    Label(t, text="location :").grid(row=3, column=0, pady=10)
    location = Entry(t)
    location.grid(row=3, column=1, sticky=W)

    Label(t, text="Priority :").grid(row=4, column=0, pady=10)
    priority = Combobox(t, values=["important", "normal"], state='readonly')
    priority.grid(row=4, column=1, sticky=W)

    Label(t, text="Date(y/m/d) :").grid(row=5, column=0, pady=10)
    year = IntVar()
    ttk.Combobox(t, textvariable=year,
                 values=list(range(2020, 2031)),
                 state='readonly').grid(row=5, column=1, sticky=W)
    month = IntVar()
    ttk.Combobox(t, textvariable=month,
                 values=list(range(1, 13)),
                 state='readonly').grid(row=5, column=2, sticky=W)
    day = IntVar()
    ttk.Combobox(t, textvariable=day,
                 values=list(range(1, 32)),
                 state='readonly').grid(row=5, column=3, sticky=W)

    Label(t, text="Time(h:m) :").grid(row=6, column=0)
    hour = IntVar()
    ttk.Combobox(t, textvariable=hour,
                 values=list(range(0, 24)),
                 state='readonly').grid(row=6, column=1, pady=10, sticky=W)
    minute = IntVar()
    ttk.Combobox(t, textvariable=minute,
                 values=list(range(0, 60)),
                 state='readonly').grid(row=6, column=2, sticky=W)
    Label(t, text="Category").grid(row=7, column=0)
    category = ttk.Combobox(t, values=['maktab', 'uni', 'home'])
    category.grid(row=7, column=1)

    set_button = Button(t, text="set", command=main).grid(row=8, column=3, pady=20, sticky=W)
    set_button = Button(t, text="subtask").grid(row=8, column=2, pady=20, sticky=E)

    t.mainloop()


def exit():
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


t = Tk()
t.geometry("300x300")
t.title("Menu")
edit_button = Button(t, text="edit", command=edit).grid(row=1, column=0)
remove_button = Button(t, text="remove").grid(row=2, column=0)
new_button = Button(t, text="new", command=new).grid(row=3, column=3)
exit_button = Button(t, text="exit", command=exit).grid(row=3, column=1)
t.mainloop()
