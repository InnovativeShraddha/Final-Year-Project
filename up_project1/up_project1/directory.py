import os
import subprocess
from subprocess import *
from os import *
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import sys
import t1

#if sys.version_info[0] < 3:
#	import Tkinter as Tk
#else:
#	import tkinter as Tk


class Serversettings:
	def __init__(self, master):
		self.master = master
		self.nb=ttk.Notebook(self.master)
		self.dirtext=StringVar()

		# Basic frame
		self.basic=ttk.Frame(self.nb)

		self.per_list=StringVar(self.basic)
		self.per_list.set("Select Permission")

		self.directory=Label(self.basic,text="Directory: ",font='bold')
		self.directoryname=Entry(self.basic,width=25, textvariable=self.dirtext)
		self.browsebtn=Button(self.basic, text = "Browse", command=self.browse_fun)
		self.share=Label(self.basic, text = "Share name :",font='bold')
		self.sharename=Entry(self.basic,width=25)
		self.desc=Label(self.basic, text = "Description :",font='bold')
		self.descentry=Entry(self.basic,width=25)

		#self.crtdir=Label(self.basic, text="OR")
		
		# to create new directory
		self.crtdirectory=Label(self.basic,text="Creat Directory: ",font='bold')
		self.crtdirectoryname=Entry(self.basic,width=25)
		self.crtdir_btn=Button(self.basic, text = "Create",command=self.createdir)

		#permission for directory

		self.choose_Per=Label(self.basic,text="Permissions:",font='bold')
		self.choose_entry=OptionMenu(self.basic,self.per_list,"Select Permission","read", "write", "execute",command=self.permissionFun)

		self.cancelbtn= Button(self.master, text= "Cancel", command=self.close_window)
		
		#directory code here
		self.okbtn= Button(self.master, text= "Ok",command=self.app_in_file)

		self.directory.grid(row=0,column=0,pady=4,padx=2)
		self.directoryname.grid(row=0,column=1,pady=4,padx=1)
		self.browsebtn.grid(row=0,column=2,pady=4,padx=5)
		self.share.grid(row=1,column=0,pady=2,padx=3)
		self.sharename.grid(row=1,column=1,pady=2,padx=2)
		self.desc.grid(row=2,column=0,pady=2,padx=3)
		self.descentry.grid(row=2,column=1,padx=2,pady=2)
		self.choose_Per.grid(row=3,column=0,padx=2,pady=4)
		self.choose_entry.grid(row=3,column=1,padx=1,pady=4)
		self.cancelbtn.grid(row=1,column=0,pady=2,ipadx=2)
		self.okbtn.grid(row=1,column=1,pady=2,ipadx=2)

		#self.crtdir.grid(row=5,column=0,pady=4)
		self.crtdirectory.grid(row=6,column=0,pady=4,padx=1)
		self.crtdirectoryname.grid(row=6,column=1,pady=4,padx=1)
		self.crtdir_btn.grid(row=6,column=2,pady=4,padx=5)


		#Access frame

		self.nb.add(self.basic,text='Basic')
		#self.nb.add(self.access,text='Access')
		self.nb.grid(row=0,column=0)

		self.w = 550 # width for the Tk root
		self.h = 250 # height for the Tk root

		self.ws = self.master.winfo_screenwidth() # width of the screen
		self.hs = self.master.winfo_screenheight() # height of the screen

		self.x = (self.ws/2) - (self.w/2)
		self.y = (self.hs/2) - (self.h/2)

		# set the dimensions of the screen
		# and where it is placed
		self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))


	def close_window(self):
		self.master.destroy()

	def browse_fun(self):
		self.master.withdraw()
		self.fname=filedialog.askdirectory()
		self.dirtext.set(self.fname)
		self.master.deiconify()

	def createdir(self):
		self.crt_name_text=self.crtdirectoryname.get()
		os.mkdir(self.crt_name_text)
		print(self.crt_name_text," created successfully")
		self.smb_command="chcon -t share_share_t"
		self.p=subprocess.Popen([self.smb_command,self.crt_name_text],shell=True,stderr=subprocess.PIPE)
		self.output,self.err=self.p.communicate()
		print("context changed ",self.output)
		self.at=subprocess.Popen(["ls -z",self.crt_name_text],shell=True,stderr=subprocess.PIPE)
		self.out,self.er=self.at.communicate()

	def permissionFun(self,value):
		print("selected ",value)
	def app_in_file(self):
		#with open("/home/abc.txt") as f:
			#self.f.write(self.directoryname.get())
			#self.f.write(self.shareame.get())
			#self.f.write(self.crtdirectoryname().get())
			#self.f.close()	
			self.app_command="echo "+self.sharename.get()+">> abc.txt"
			self.p=subprocess.Popen(self.app_command,self.name,shell=True,stderr=subprocess.PIPE)
			self.output,self.err=self.p.communicate()

