try:
	from Tkinter import *
	from ttk import *
except ImportError:  # Python 3
	from tkinter import *
	from tkinter.ttk import *
	from tkinter import ttk
	from tkinter import font
	from tkinter import messagebox
	import install
	import HelpClass
	import directory
	import sambaUsers
	import services
	import share

class App(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.CreateUI()
		#self.LoadTable()
		self.grid(sticky = (N,S,W,E))

		parent.grid_rowconfigure(0, weight = 1)
		parent.grid_columnconfigure(0, weight =1)
		
		#menubar
	  
		self.menubar=Menu(self)
		
		self.installmenu=Menu(self.menubar,tearoff=0)
		self.menubar.add_cascade(label="Install",menu=self.installmenu,activebackground='cornsilk2',font='ariel')
		self.installmenu.add_command(label="Install Packages",activebackground='PeachPuff3',font='ariel',command=self.install)
	
		self.editmenu=Menu(self.menubar,tearoff=0)
		self.menubar.add_cascade(label="Preferences",menu=self.editmenu,activebackground="lightblue",font="ariel")
		self.editmenu.add_command(label="server settings",activebackground="lightblue",font="ariel",command=self.serverWindow)
		self.editmenu.add_command(label="samba users",activebackground="lightblue",font="ariel",command=self.sambausers)
		self.editmenu.add_command(label="Sharing of files",activebackground="lightblue",font="ariel",command=self.share_file)


		self.services=Menu(self.menubar,tearoff=0)
		self.menubar.add_cascade(label="Services",menu=self.services,activebackground="lightblue",font="ariel")
		self.services.add_command(label="Start",activebackground="lightblue",font="ariel",command=self.Services)


		self.helpmenu=Menu(self.menubar,tearoff=0)
		self.menubar.add_cascade(label="About",menu=self.helpmenu,activebackground="lightyellow",font="ariel")
		self.helpmenu.add_command(label="Help",activebackground="lightblue",font="ariel",command=self.help)
		self.master.config(menu=self.menubar)


	def CreateUI(self):
		tv = Treeview(self)
		tv['columns'] = ('Directory', 'Share name', 'Permissions','Visibility','Description')
		tv.heading("#0", text= 'Sr.No')
		tv.column("#0", anchor='w', width=20)
		tv.heading('Directory', text='Directory', anchor='w')
		tv.column('Directory', anchor="w")
		tv.heading('Share name', text='Share name')
		tv.column('Share name', anchor='center', width=150)
		tv.heading('Permissions', text='Permissions')
		tv.column('Permissions', anchor='center', width=150)
		tv.heading('Visibility', text='Visibility')
		tv.column('Visibility', anchor='center', width=150)
		tv.heading('Description',text='Descripion')
		tv.column('Description', anchor='center', width=150)
		tv.grid(sticky = (N,S,W,E))
		self.treeview = tv
		self.grid_rowconfigure(0, weight = 1)
		self.grid_columnconfigure(0, weight = 1)
		self.i = 1

	def install(self):
		self.installpack=Toplevel(self)
		self.installpack.title("Install SambaPackages")
		self.inusr=install.Install(self.installpack)

	def Services(self):
		self.servicepack=Toplevel(self)
		self.servicepack.title("Samba Services")
		self.service=services.Services(self.servicepack)

	#def LoadTable(self):
        	#self.treeview.insert('','end', text=str(self.i), values=('90', '10:10', 'Ok'))
        	#self.i = self.i + 1
	
	def serverWindow(self):
		self.newWindow = Toplevel(self)
		self.newWindow.title("Server Settings")
		self.app = directory.Serversettings(self.newWindow)

	def sambausers(self):
		self.smbuser=Toplevel(self)
		self.smbuser.title("Samba Users")
		self.smusr=sambaUsers.SambaUser(self.smbuser)
	
	def help(self):
		self.help=Toplevel(self)
		self.help.title("Help And About Us")
		self.help1=HelpClass.HelpClass(self.help)

	def share_file(self):
		self.f=Toplevel(self)
		self.f.title("Share Files")
		self.f1=share.Share(self.f)

def main():
	root = Tk()
	w = 950 # width for the Tk root
	h = 550 # height for the Tk root

	ws = root.winfo_screenwidth() # width of the screen
	hs = root.winfo_screenheight() # height of the screen

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	# set the dimensions of the screen 
	# and where it is placed
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#root.geometry("950x550+0+0")
	root.title("samba server configuration")
	App(root)
	root.mainloop()

if __name__ == '__main__':
    main()
