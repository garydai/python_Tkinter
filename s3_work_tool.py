#-*- encoding=UTF-8 -*-
from Tkinter import *
import os
class App:
    def __init__(self, master):
        self.button1 = Button(master, text="run_server_floder", command=self.open_run_server_floder)
        self.button1.pack() 
        self.botton2 = Button(master, text="log_floder", command=self.open_log_floder)
        self.botton2.pack()
        self.botton3 = Button(master, text="testkit_log_floder", command=self.open_testkit_log_floder)
        self.botton3.pack()
        self.botton4 = Button(master, text="grammar_debug_floder", command=self.open_grammar_debug_floder)
        self.botton4.pack()
        self.botton5 = Button(master, text="run_test_floder", command=self.open_run_test_debug_floder)
        self.botton5.pack()

    def open_run_server_floder(self):
		start_directory = r'D:\p4_scm-shanghai.s3graphics.com2666_garydai-x64\Voice\nlp\Source\AppDevbuild\bin\Debug_x64\server'
		os.system("explorer.exe %s" % start_directory)
    def open_log_floder(self):
		start_directory = r'D:\p4_scm-shanghai.s3graphics.com2666_garydai-x64\Voice\nlp\Source\AppDevbuild\bin\Debug_x64\server\log'
		os.system("explorer.exe %s" % start_directory)
    def open_testkit_log_floder(self):
		start_directory = r'D:\p4_scm-shanghai.s3graphics.com2666_garydai-x64\Voice\nlp\Source\dstestkit\TestSet'
		os.system("explorer.exe %s" % start_directory)
    def open_grammar_debug_floder(self):
		start_directory = r'D:\p4_scm-shanghai.s3graphics.com2666_garydai-x64\Voice\nlp\Source\AppDevbuild\bin\Debug_x64\tools'
		os.system("explorer.exe %s" % start_directory)
	
    def open_run_test_debug_floder(self):
		start_directory = r'D:\p4_scm-shanghai.s3graphics.com2666_garydai-x64\Voice\nlp\Source\AppDevbuild\bin\Debug_x64\TestTools'
		os.system("explorer.exe %s" % start_directory)
		
if __name__ == '__main__':

	win = Tk()
	win.geometry('400x200')

	app = App(win)
	win.mainloop()