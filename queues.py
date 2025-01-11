import time
import datetime
import subprocess

from tkinter import *
from classes.projectClass import Project
from classes.userClass import User
from classes.timerClass import Timer
from classes.taskClass import Task
import se

#Главна страница с информация за потребителя
#Всички негови проекти са показани в дясно
#Проеките са изобразени като бутони, за лесен достъп до тях

timer = Timer(0)
user = User("", "", 0, "", "", "")
user_details = user.getUser(1)
user = User(user_details[0][1], user_details[0][3], user_details[0][2], 
	user_details[0][4], user_details[0][6], user_details[0][5])
time_label = None

root = Tk()
root.title('Проекти')
root.geometry('{}x{}'.format(960, 500))

def open_form():
	root.destroy()
	subprocess.run(["python3", "forms_project.py"])	

def open_project(idp):
	se.ids["project_id"] = idp
	print(se.ids)
	root.destroy()
	subprocess.run(["python3", "projects.py"])

def user_open():
	root.destroy()
	subprocess.run(["python3", "userpage.py"])	

# create all of the main containers
top_frame = Frame(root, bg='light sky blue', width=450, height=50, pady=3)
center = Frame(root, bg='black', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
btm_frame2 = Frame(root, bg='sky blue', width=450, height=60, pady=3)

ctr_left = Frame(center, bg='white', width=200, height=190, padx=3, pady=3)
ctr_right = Frame(center, bg='light sky blue', width=200, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="nsew")
ctr_right.grid(row=0, column=1, sticky="nsew")

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")

# create the widgets for the top frame'
user_label = Button(top_frame, text='Излизане от профил', command=user_open)
model_label = Label(ctr_left, text='Потребител данни:')#info about project form DB
model_labels = Label(ctr_left, text=('Потребител: ' + str(user.getName()) + 
'\n' + 'Фирма име: ' + str(user.getFirm()) + 
'\n' + 'Email адрес: ' + str(user.getEmail()) +
'\n' + 'Телефонен номер: ' + str(user.getPhone())))#info about user form DB
width_label = Label(top_frame, text='Проекти на потребител ' + str(user.getName()))# Get project name from DB

send_label = Button(top_frame, text='Започни нов проект', command=open_form)#open small form for new task creation

langs = []
project_list = Project("", "", "", "").getFromDB(se.ids["user_id"])
k = 0
for i in project_list:
	langs.append("Име на проект: "+str(i[2])+"; Фирма: "+str(i[4])+"; Локация: "+str(i[5]))
	button = Button(ctr_right, text = langs[-1], command = lambda x=i[0] : open_project(x))	
	button.grid(row=k, column=0, sticky = W)
	k+=1

# layout the widgets in the top frame
user_label.grid(row=0, column=0)
model_label.grid(row=0, columnspan=3)
model_labels.grid(row=1)
width_label.grid(row=1, column=2)
send_label.grid(row=1,column=0)

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

def update():
	if True:
		langs = []
		project_list = Project("", "", "", "").getFromDB(se.ids["user_id"])
		for i in project_list:
			langs.append("Име на проект: "+str(i[2])+"; Фирма: "+str(i[4])+"; Локация: "+str(i[5]))
			button = Button(ctr_right, text = langs[-1], command = lambda x=i[0] : open_project(x))		

		root.after(100, update)

update()
root.mainloop()
