import time
import datetime
import subprocess

#Страница на проект
#Дава информация за проекта
#Списък със задачите за този проект

from tkinter import *
from classes.timerClass import Timer
from classes.commentClass import Comment
from classes.taskClass import Task
from classes.projectClass import Project
import se

timer = Timer(0)
comment_list = []
langs = []
time_label = None

project = Project("", "", "", "")
projest_list = project.getFromDB(se.ids["user_id"])

root = Tk()
root.title('Задачи')
root.geometry('{}x{}'.format(960, 500))

def open_queue():
	root.destroy()
	subprocess.run(["python3", "queues.py"])

def open_form():
	root.destroy()
	subprocess.run(["python3", "forms_tasks.py"])

def open_task(idt):
	root.destroy()
	se.ids["task_id"] = idt
	subprocess.run(["python3", "tasks.py"])

def open_user():
	root.destroy()
	subprocess.run(["python3", "userpage.py"])

def text_coded():
	space = 0
	signs = 0
	txt = str(projest_list[0][3])
	for sign in txt:
		signs+=1
		if sign == " ":
			space+=1
		if space == 3:
			space = 0
			txt = txt[ : signs]+'\n'+txt[signs : ]

	return txt			


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
home_label = Button(top_frame, text='Главна страница', command=open_queue)
user_label = Button(top_frame, text='Излизане от профил', command=open_user)
model_label = Label(ctr_left, text='Проект:')#info about project form DB
model_labels = Label(ctr_left, text=text_coded())#info about project form DB
width_label = Label(top_frame, text='Задачи по проект '+str(projest_list[0][2]))# Get project name from DB

send_label = Button(top_frame, text='Добави нова задача', command=open_form)#open small form for new task creation

langs = []
tasks_list = Task("", "", "", "", se.ids["project_id"]).getFromDB()
k = 0
for i in tasks_list:
	if i[6] > datetime.datetime.now().date():
		passed = " "
		c = "black"
	else:
		passed = "*пропусната*"
		c = "red"

	langs.append("Задача: "+str(i[7])+"; Крайна дата:"+passed+str(i[6])+"; За правене: "+str(i[4])+"; Готови: "+str(i[3]))
	button = Button(ctr_right, text = langs[-1], fg=c, command = lambda x=i[0] : open_task(x))	
	button.grid(row=k, column=0, sticky = W)
	k+=1

# layout the widgets in the top frame
home_label.grid(row=0, column=1)
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
		root.after(100, update)

update()
root.mainloop()
