#-*- encoding=UTF-8 -*-
from Tkinter import *
import os
class App:
    def __init__(self, master):
        self.button1 = Button(master, text="server_floder", command=self.open_server_floder)
        self.button1.pack() 
        self.botton2 = Button(master, text="log_floder", command=self.open_log_floder)
        self.botton2.pack()
        self.botton3 = Button(master, text="test_log_floder", command=self.open_test_log_floder)
        self.botton3.pack()

    def open_server_floder(self):
		start_directory = r'D:'
		os.system("explorer.exe %s" % start_directory)
    def open_log_floder(self):
		start_directory = r'D:'
		os.system("explorer.exe %s" % start_directory)
    def open_test_log_floder(self):
		start_directory = r'D:'
		os.system("explorer.exe %s" % start_directory)

if __name__ == '__main__':

	win = Tk()
	win.geometry('400x200')

	app = App(win)
	win.mainloop()