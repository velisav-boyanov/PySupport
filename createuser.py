import tkinter
from tkinter import messagebox
from classes.userClass import User
import se
import subprocess

window = tkinter.Tk()
window.title("Login form")
window.geometry('1140x540')
window.configure(bg='light sky blue')

def register():
    username = username_entry.get()
    email = email_entry.get()
    firm = firm_entry.get()
    second_name = second_name_entry.get()
    phone = phone_entry.get()
    password = password_entry.get()
    user = User(username, second_name, password, firm, phone, email)
    se.ids["user_id"] = user.createUser()
    print(se.ids["users_id"])
    window.destroy()
    subprocess.run(["python3", "queues.py"])


frame = tkinter.Frame(bg='light sky blue')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Регистрация", bg='light sky blue', fg="blue", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Потребителско име", bg='light sky blue', fg="white", font=("Arial", 16))
email_label = tkinter.Label(
    frame, text="Имейл", bg='light sky blue', fg="white", font=("Arial", 16))
firm_label = tkinter.Label(
    frame, text="Фирма име", bg='light sky blue', fg="white", font=("Arial", 16))
second_name_label = tkinter.Label(
    frame, text="Второ име", bg='light sky blue', fg="white", font=("Arial", 16))
phone_label = tkinter.Label(
    frame, text="Телефонен номер", bg='light sky blue', fg="white", font=("Arial", 16))

username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
email_entry = tkinter.Entry(frame, font=("Arial", 16))
firm_entry = tkinter.Entry(frame, font=("Arial", 16))
phone_entry = tkinter.Entry(frame, font=("Arial", 16))
second_name_entry = tkinter.Entry(frame, font=("Arial", 16))

password_label = tkinter.Label(
    frame, text="Парола", bg='light sky blue', fg="white", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Вход", bg="blue", fg="white", font=("Arial", 16), command=register)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
email_entry.grid(row=2, column=3, pady=20)
firm_entry.grid(row=1, column=3, pady=20)
phone_entry.grid(row=3, column=1)
second_name_entry.grid(row=3, column=3, pady=20)
email_label.grid(row=2, column=2,pady=20)
firm_label.grid(row=1, column=2)
phone_label.grid(row=3, column=0)
second_name_label.grid(row=3, column=2, pady=20)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=4, column=2, columnspan=2, pady=30)

frame.pack()

window.mainloop()