import tkinter
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime 
import subprocess
from tkcalendar import DateEntry

from classes.taskClass import Task
from se import user_id
from se import project_id

window = tkinter.Tk()
window.title("Форма за създаване на задача")

frame = tkinter.Frame(window)
frame.pack()

def create_tasks():
    text = text_entry.get()
    done = done_entry.get()
    tobe = tobe_entry.get()
    selected_date = cal.get_date()
    task = Task(text, tobe, done, selected_date, user_id)
    task.saveToDB(project_id)
    window.destroy()
    subprocess.run(["python3", "projects.py"])

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="Данни за фирма изпълнител")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

date_label = tkinter.Label(user_info_frame, text="Краен Срок:")
date_label.grid(row=0, column=1)
cal = DateEntry(user_info_frame, width=12, background="darkblue", foreground="white", borderwidth=2)
cal.grid(row=1, column=1)
text_label = tkinter.Label(user_info_frame, text="Задача:")
text_label.grid(row=0, column=0)
done_label = tkinter.Label(user_info_frame, text="Завършени до този момент подзадачи.    ")
done_label.grid(row=2, column=0)
tobe_label = tkinter.Label(user_info_frame, text="Предстоящи подзадачи брой.     ")
tobe_label.grid(row=2, column=1)

text_entry = tkinter.Entry(user_info_frame, width = 100)
text_entry.grid(row=1, column=0)
done_entry = tkinter.Entry(user_info_frame)
tobe_entry = tkinter.Entry(user_info_frame)
done_entry.grid(row=3, column=0)
tobe_entry.grid(row=3, column=1)


# Button
button = tkinter.Button(frame, text="Продължи", command=create_tasks)
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()