
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk
else:
	import tkinter as Tk

class Share:
	def __init__(self, master):
		self.master = master
		self.nb=ttk.Notebook(self.master)

		# Basic frame
		self.share=ttk.Frame(self.nb)
		self.filenames=""  #variable to store filename
		self.v=StringVar()

		self.file=Label(self.share,text="Select File: ",font='bold')
		self.filename=Entry(self.share,width=25, textvariable=self.v)
		self.browse_file=Button(self.share, text = "Browse File", command=self.browse_fun)


		#self.crtfile=Label(self.share,text="Creat file: ",font='bold')
		#self.crtfilename=Entry(self.share,width=25)
		#self.crtfile_btn=Button(self.share, text = "Create file")

		self.cancelbtn= Button(self.share, text= "Cancel", command=self.close_window)
		self.share_btn=Button(self.share,text="Share")
		
		self.file.grid(row=0,column=0,pady=4,padx=2)
		self.filename.grid(row=0,column=1,pady=4,padx=1)
		self.browse_file.grid(row=0,column=2,pady=4,padx=5)
		self.cancelbtn.grid(row=1,column=0,pady=2,padx=3)
		self.share_btn.grid(row=1,column=1,pady=2,padx=2)
		self.nb.add(self.share,text='Share')
		self.nb.grid(row=0,column=0)

		self.w = 450 # width for the Tk root
		self.h = 150 # height for the Tk root

		self.ws = self.master.winfo_screenwidth() # width of the screen
		self.hs = self.master.winfo_screenheight() # height of the screen

		self.x = (self.ws/2) - (self.w/2)
		self.y = (self.hs/2) - (self.h/2)

		# set the dimensions of the screen
		# and where it is placed
		self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

	def browse_fun(self):
		#self.master.overrideredirect(1)
		self.master.withdraw()
		self.fname=filedialog.askopenfilename(filetypes= (("Templates files", "*.type"), ("All files","*")))
		self.v.set(self.fname)
		self.master.deiconify()
	
	def close_window(self):
		self.master.destroy()

