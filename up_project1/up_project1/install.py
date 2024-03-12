from tkinter import *
from subprocess import call
import subprocess
from tkinter.ttk import *
from tkinter import ttk

class Install:
	def __init__(self, master):
		#Toplevel.__init__(self,master)
		self.master = master
		self.nb=ttk.Notebook(self.master,height=200,width=350)
		
		# install frame
		self.install=ttk.Frame(self.nb)
		self.label = Label(self.install, text="Install and Uninstall samba from here!")
		self.label.grid(row=0,column=0,pady=1,padx=1)
		
		self.install_btn = Button(self.install, text="INSTALL", command=self.instal)
		self.install_btn.grid(row=1,column=0,padx=2,pady=2)

		self.uninstall_btn = Button(self.install, text="UNINSTALL", command=self.uninstal)
		self.uninstall_btn.grid(row=1,column=1,padx=2,pady=2)


		self.close_button = Button(self.master, text="Close", command=self.close_window)
		self.close_button.grid(row=2,column=0,pady=3)

		self.nb.add(self.install,text='Install')
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

		

	def instal(self):
		self.smb_command="yum install samba samba-client cifs-utils -y"
		self.p=subprocess.Popen(self.smb_command,shell=True,stderr=subprocess.PIPE)
		self.output,self.err=self.p.communicate()

	def uninstal(self):
		self.smb_command="yum remove samba samba-client cifs-utils -y"
		self.p=subprocess.Popen(self.smb_command,shell=True,stderr=subprocess.PIPE)
		self.output,self.err=self.p.communicate()

	def close_window(self):
		self.master.destroy()

