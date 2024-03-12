
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import font


class HelpClass:
	def __init__(self, master):
		self.font1=font.Font(family="Helvetica", size=15,slant=font.ITALIC)
		self.master = master
		self.nb=ttk.Notebook(self.master)

		# Basic frame
		self.basic=ttk.Frame(self.nb)
		
		self.help= """To Configure a Samba Server you need to perform following steps:
        1)Check Samba Packages are installed on your system or not.
        to check go to menu install--> install packages.
        2)configure samba with filling proper details.
        ** if you have any query mail us:
        vidyahonde1997@gmail.com"""

		self.help=Label(self.basic,text=self.help,font='bold')
		self.help.grid(row=0,column=0,columnspan=3,pady=2,padx=3)
		self.nb.add(self.basic,text="Help")

		#about frame
		self.about=ttk.Frame(self.nb)
		self.msg="""
This project is relaed to Samba server configuration.
This is BE level project.
This is GUI for Samba users.

****************************
This Project is created by :
        1)Vidya Honde
        2)Shreya Patil
        3)Pratiksha Girmaji
	4)Shraddha Gardas"""

		self.label1=Label(self.about,text=self.msg,font=self.font1)
		self.button1=Button(self.master, text = "OK", width =10,command = self.close_windows)
		self.label1.grid(row=0,column=0,columnspan=3,pady=2,padx=3)
		self.button1.grid(row=1,column=1,columnspan=3,rowspan=3,padx=5,pady=2)
		self.nb.add(self.about,text="About")

		self.nb.grid(row=0,column=0,padx=2,pady=1)

		self.w = 650 # width for the Tk root
		self.h = 350 # height for the Tk root

		self.ws = self.master.winfo_screenwidth() # width of the screen
		self.hs = self.master.winfo_screenheight() # height of the screen

		self.x = (self.ws/2) - (self.w/2)
		self.y = (self.hs/2) - (self.h/2)

		# set the dimensions of the screen
		# and where it is placed
		self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))


	def close_windows(self):
		self.master.destroy()

