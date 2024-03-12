from tkinter import *
from subprocess import call
import subprocess
from tkinter.ttk import *
from tkinter import ttk

class Services:
	def __init__(self, master):
		self.master = master
		self.nb=ttk.Notebook(self.master,height=200,width=350)
		
		# install frame
		self.service=ttk.Frame(self.nb)
		self.label = Label(self.service, text="Start samba services from here!")
		self.label.grid(row=0,column=0,pady=4,padx=3)
		
		
		self.service_btn = Button(self.service, text="Start", command=self.start_service)
		self.service_btn.grid(row=1,column=0,padx=2,pady=2)

		self.enable_btn = Button(self.service, text="Enable", command=self.Enable)
		self.enable_btn.grid(row=2,column=0,padx=2,pady=2)

		self.firewall_btn = Button(self.service, text="Firewall", command=self.Firewall)
		self.firewall_btn.grid(row=3,column=0,padx=2,pady=2)

		self.reload_btn = Button(self.service, text="Reload", command=self.reload)
		self.reload_btn.grid(row=4,column=0,padx=2,pady=2)
				

		self.close_button = Button(self.master, text="Close", command=self.close_window)
		self.close_button.grid(row=1,column=1,pady=3)

		self.nb.add(self.service,text='Services')
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

	def start_service(self):
		print("hello")
		self.smb_command="systemctl restart smb nmb"
		self.p=subprocess.Popen(self.smb_command,shell=True,stderr=subprocess.PIPE)
		self.output,self.err=self.p.communicate()
	
	def Enable(self):
		print("enable")
		self.smb_command="systemctl enable smb nmb"
		self.p=subprocess.Popen(self.smb_command,shell=True,stderr=subprocess.PIPE)
		self.output,self.err=self.p.communicate()
		print(str(self.output)+" "+str(self.err))

	def Firewall(self):
		print("firewall")
		self.smb_command="firewall-cmd --permanent --add-service=samba"
		self.p=subprocess.Popen(self.smb_command,shell=True,stderr=subprocess.PIPE)
		self.output,self.err=self.p.communicate()

	def reload(self):
		print("reload")
		self.smb_command="firewall-cmd --relaod"
		self.p=subprocess.Popen(self.smb_command,shell=True,stderr=subprocess.PIPE)
		self.output,self.err=self.p.communicate()	

	def close_window(self):
		self.master.destroy()
