import tkinter
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime 
import subprocess

from classes.projectClass import Project
from se import user_id
from se import project_id

window = tkinter.Tk()
window.title("Форма за създаване на проект")

frame = tkinter.Frame(window)
frame.pack()

def create_tasks():
    name = name_entry.get()
    location = location_entry.get()
    firm = firm_entry.get()
    desc = desc_entry.get()
    project = Project(name, location, firm, desc)
    project.saveToDB(user_id)
    window.destroy()
    subprocess.run(["python3", "queues.py"])

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="Данни за фирма изпълнител")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

name_label = tkinter.Label(user_info_frame, text="Име на проект:")
name_label.grid(row=0, column=0)
desc_label = tkinter.Label(user_info_frame, text="Описание на проекта:")
desc_label.grid(row=0, column=1)
location_label = tkinter.Label(user_info_frame, text="Адрес.    ")
location_label.grid(row=2, column=0)
firm_label = tkinter.Label(user_info_frame, text="Фирма изпълнител.     ")
firm_label.grid(row=2, column=1)

name_entry = tkinter.Entry(user_info_frame)
name_entry.grid(row=1, column=0)
desc_entry = tkinter.Entry(user_info_frame, width=50)
desc_entry.grid(row=1, column=1)
location_entry = tkinter.Entry(user_info_frame)
firm_entry = tkinter.Entry(user_info_frame)
location_entry.grid(row=3, column=0)
firm_entry.grid(row=3, column=1)


# Button
button = tkinter.Button(frame, text="Продължи", command=create_tasks)
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()