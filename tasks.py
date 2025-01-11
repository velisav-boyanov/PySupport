
import time
from datetime import datetime 
import subprocess
from PIL import Image, ImageTk

from tkinter import Tk, Button, Frame, Label, Entry, Variable, Listbox, EXTENDED
from classes.timerClass import Timer
from classes.commentClass import Comment
from classes.taskClass import Task
import se

#Страница на задача и с информация за нея в ляво
#Поле за коментари в центъра
#Таймер и бутон за завършване на подзадача

timer = Timer(0)
comment_list = []
langs = []
time_label = None
task = Task("", 0, 0, datetime.now(), se.ids["task_id"])
task_details = task.getFromDB()
#print(task_details[0])
timer.getFromDB(se.ids["task_id"])

def startTime():
	timer.startTime()

def endTime():
	timer.endTime()
	timer.saveToDB(se.ids["task_id"])

def add_comment():
	content = entry_W.get()
	user = se.ids["user_id"]
	task = se.ids["task_id"]
	time_of = datetime.now()
	com = Comment(user, task, content, time_of)
	com.saveToDB()

root = Tk()
root.title('Задача')
root.geometry('{}x{}'.format(960, 500))

def increment_work():
	task_h = Task("", 0, 0, datetime.now(), se.ids["task_id"])
	task_detail = task_h.getFromDB()

	if task_detail[0][4] != 0:
		task_h.incrementDB(se.ids["task_id"])

def make_time():
	h = 0
	m = 0

	t = int(timer.getTime())	

	while True:
		if t >= 3600:
			t-=3600
			h+=1
			continue
		elif t >= 60:
			t-=60
			m+=1
			continue
		else:
			break		

	res = str(h)+"ч."+str(m)+"м."+str(t)+"с."

	return res

def open_user():
	root.destroy()
	subprocess.run(["python3", "userpage.py"])

def open_queue():
	root.destroy()
	subprocess.run(["python3", "queues.py"])

# create all of the main containers
top_frame = Frame(root, bg='light sky blue', width=450, height=50, pady=3)
center = Frame(root, bg='black', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='white', width=450, height=45, pady=3)
btm_frame2 = Frame(root, bg='sky blue', width=450, height=60, pady=3)

ctr_left = Frame(center, bg='white', width=200, height=190)
ctr_mid = Frame(center, bg='light sky blue', width=250, height=190, padx=3, pady=3)
ctr_right = Frame(center, bg='white', width=200, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")

# create the widgets for the top frame
home_label = Button(top_frame, text='Главна страница', command=open_queue)
user_label = Button(top_frame, text='Влизане в профил', command=open_user)
work_done = Button(ctr_right, text='Добави завършена подзадача', command=increment_work)
model_label = Label(ctr_left, text='Име на задача')# Take from DB
task_label = Label(ctr_left, text=str(task_details[0][7]))#Take from DB
model1_label = Label(ctr_left, text='Завършени: ')# Take from DB
task1_label = Label(ctr_left, text=str(task_details[0][3]))#Take from DB
model2_label = Label(ctr_left, text='Останали: ')# Take from DB
task2_label = Label(ctr_left, text=str(task_details[0][4]))#Take from DB
model3_label = Label(ctr_left, text='Начална дата: ')# Take from DB
task3_label = Label(ctr_left, text=str(task_details[0][6]))#Take from DB
#KOPCHETA ZA HODENE PO DRUGI STRANICI NA ROW 0 top frame
width_label = Label(top_frame, text='Коментар:')

time_label = Label(ctr_right, text=('Отброено време: ' + make_time()))

send_label = Button(top_frame, text='Изпрати', command=add_comment)
length_label = Button(ctr_right, text='Започване на брояч', command=startTime)
stop_length_label = Button(ctr_right, text='Спиране на брояч', command=endTime)
entry_W = Entry(top_frame, background="white",width=50)
entry_W.focus_set()
#entry_W.pack()

#img = ImageTk.PhotoImage(Image.open("Pics/Screenshot from 2023-12-17 18-46-30.png").resize((200, 150)))
#panel = Label(ctr_right, image=img)
#panel.grid(row=5, pady=10)

# create the widgit for comments height=ctr_mid.winfo_height(), width=ctr_mid.winfo_width(),
var = Variable(value=langs)
listbox = Listbox(ctr_mid, listvariable=var, height=100, width=50, selectmode=EXTENDED, bg='white')
#listbox.pack(expand=True, fill=BOTH)

# layout the widgets in the top frame
home_label.grid(row=0, column=1)
user_label.grid(row=0, column=0)

work_done.grid(row=4, pady=20)
model_label.grid(row=0, columnspan=3)
task_label.grid(row=1, columnspan=4)
model1_label.grid(row=2, column=0)
task1_label.grid(row=2, column=1)
model2_label.grid(row=3, column=0)
task2_label.grid(row=3, column=1)
model3_label.grid(row=4, columnspan=3)
task3_label.grid(row=5, columnspan=4)
width_label.grid(row=1, column=0)
length_label.grid(row=1, column=0)
stop_length_label.grid(row=2, column=0)
time_label.grid(row=3, column=0)
entry_W.grid(row=1, column=1)
listbox.grid(row=0)
send_label.grid(row=1,column=2)

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

def update():
	if True:
		global time_label
		global h
		global w
		w = int(ctr_mid.winfo_width()/8.5)
		h = int(ctr_mid.winfo_height()/8.5)

		time_label.configure(text='Отброено време: ' + make_time() + " сек.")
		
		if timer.getIsOn():
			length_label.configure(text='Броячът е пуснат')	
		else:
			length_label.configure(text='Започване на брояч')

		comment_list = Comment(se.ids["user_id"], se.ids["task_id"], "", datetime.now()).getCommentsFromTask()
		langs = []
		for i in comment_list:
			user_data = Comment(se.ids["user_id"], se.ids["task_id"], "", datetime.now()).getUser()
			langs.append(str(user_data[0][0])+" "+str(user_data[0][1])+ ": "+str(i[3])+"  "+str(i[4]))

		var = Variable(value=langs)
		listbox.configure(listvariable=var, width=w, height=h)	

		task_details = Task("", 0, 0, datetime.now(), se.ids["task_id"]).getFromDB()

		task1_label.configure(text=str(task_details[0][3]))
		task2_label.configure(text=str(task_details[0][4]))

		root.after(100, update)

update()
root.mainloop()
