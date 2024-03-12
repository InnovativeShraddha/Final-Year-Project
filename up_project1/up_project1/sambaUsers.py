from tkinter import *
#from subprocess import *
import subprocess
#from os import open
import os
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox

class SambaUser:
	def __init__(self, master):
		self.master = master
		self.nb=ttk.Notebook(self.master,height=250,width=430)
		
		self.usr=ttk.Frame(self.nb,height=250,width=440)

		self.usrname = Label(self.usr,text="Username")
		self.usrname.grid(row=1,column=0,padx=2,pady=6)

		self.usr_list=StringVar(self.usr)
		self.a=[]
		self.line=[]
		self.line1=[]
		with open("/etc/passwd","r") as f:
			self.line=f.read().splitlines()

		for i in range(0,len(self.line)):
			self.line1.append(self.line[i].split(":"))
			if(self.line1[i][6]=='/bin/bash'):
				self.a.append(self.line1[i][0].split(":"))
		self.usr_list.set(self.a[0])

		self.usr_nam= Entry(self.usr,width=25)
		self.usr_nam.grid(row=1,column=1,padx=2,pady=6)

		self.usr_pass = Label(self.usr,text="Password")
		self.usr_pass.grid(row=2,column=0,padx=1,pady=6)

		self.pass_nam= Entry(self.usr,width=25,show="*")
		self.pass_nam.grid(row=2,column=1,padx=2,pady=6)

		self.cnf_pass = Label(self.usr,text="Confirm Password")
		self.cnf_pass.grid(row=3,column=0,padx=1,pady=4)

		self.cnf_pass= Entry(self.usr,width=25,show="*")
		self.cnf_pass.grid(row=3,column=1,padx=2,pady=4)

		self.usradd_btn = Button(self.usr, text="Add User",command=self.addUser)
		self.usradd_btn.grid(row=5,column=0,padx=1,pady=3)

		self.close_button = Button(self.usr, text="Cancel", command=self.close_window)
		self.close_button.grid(row=8,column=1,pady=8)

		self.del_usr= Button(self.usr, text="Delete User",command=self.del_user)
		self.del_usr.grid(row=8,column=2,pady=8)


		self.select = Label(self.usr,text="Select User")
		self.select.grid(row=7,column=0,padx=1,pady=4)
		
		self.select_entry= OptionMenu(self.usr,self.usr_list,"Select user",*(self.a),command=self.permissionFun)
		self.select_entry.grid(row=7,column=1,padx=1,pady=4)

		#self.add_btn = Button(self.usr, text="Select User")
		#self.add_btn.grid(row=8,column=0,padx=1,pady=5)

		self.nb.add(self.usr,text='User Configuaration')
		self.nb.grid(row=0,column=0)

		self.w = 450 # width for the Tk root
		self.h = 300 # height for the Tk root

		self.ws = self.master.winfo_screenwidth() # width of the screen
		self.hs = self.master.winfo_screenheight() # height of the screen

		self.x = (self.ws/2) - (self.w/2)
		self.y = (self.hs/2) - (self.h/2)

		# set the dimensions of the screen
		# and where it is placed
		self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

	def addUser(self):
		self.a=[]
		self.line=[];
		self.line1=[];
		
		with open("/etc/passwd") as f:
		 self.line=f.read().splitlines()
		
		for i in range(0,len(self.line)):
			self.line1.append(self.line[i].split(":"))
			if(self.line[i][6]=='bin/bash'):
			    self.a.append(self.line1[i][0].split(":"))
		
		for i in range(0,len(self.a)):
			self.s=str(self.a[i])
			self.new_s=self.s[2:len(self.s)-2]
			if (self.usr_name == self.new_s):
				print("user already exist")
				Message(self, "username already Exist")

			print(self.a[i])
			print("and self.s="+str(self.s))
			print(self.new_s)
		os.system("useradd "+str(self.usr_nam.get()))
		print(str(self.usr_nam.get()),"user added")

			
	def msg(self):
		messagebox.showinfo("Username", "username already Exist")
		
	def addOption(self, label):
		self["menu"].add_command(label=label,
		command=tk._setit(variable, label, self._command))


	def close_window(self):
		self.master.destroy()

	def permissionFun(self,value):
		
		self.option_item_list=value
		#self.usr_name_value=self.option_item_list[0]
		print(self.option_item_list[0])

	def del_user(self):
		#self.smb_command='userdel -r'
		os.system("userdel -r %s" %(self.option_item_list[0]))
		#print("user deleted"+" "+str(self.option_item_list))
		print(self.option_item_list[0],"user deleted")
		#self.p=subprocess.Popen([self.smb_command,self.option_item_list[0]],shell=True,stderr=subprocess.PIPE)
		#self.output,self.err=self.p.communicate()
		#print("user deleted %s" % self.option_item_list[0])


	def crt_user(self):
		self.usr_name=self.usr_nam.get()
		self.usr_password=self.pass_nam.get()
		self.cnf_password=self.cnf_pass.get()
#		proc=Popen(['usr/bin/sudo','/usr/bin/passwd',self.usr_name, '--d'])
		if(self.usr_password == self.cnf_password):
			proc=Popen(['sudo', 'smbpasswd', '-a', '-s', self.usr_name], stdin=subprocess.PIPE)
			proc.communicate(input=self.usr_password+ '\n'+ self.usr_password)
			print("password set")
#               os.system("useradd  %s "%(self.usr_name))
#                       print("password set")

