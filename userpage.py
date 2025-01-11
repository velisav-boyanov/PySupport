import tkinter
from tkinter import messagebox
import subprocess

window = tkinter.Tk()
window.title("Login form")
window.geometry('640x440')
window.configure(bg='light sky blue')

def open_register():
    window.destroy()
    subprocess.run(["python3", "createuser.py"])

def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Вход успешен", message="Успешно влезнахте в профила си.")
    else:
        messagebox.showerror(title="Грешка", message="Невалидни данни.")

frame = tkinter.Frame(bg='light sky blue')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Вход", bg='light sky blue', fg="blue", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Потребителско име", bg='light sky blue', fg="white", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Парола", bg='light sky blue', fg="white", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Вход", bg="blue", fg="white", font=("Arial", 16), command=login)
register_button = tkinter.Button(
    frame, text="Създай профил", bg="blue", fg="white", font=("Arial", 16), command=open_register)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0)
register_button.grid(row=3, column=1)

frame.pack()

window.mainloop()