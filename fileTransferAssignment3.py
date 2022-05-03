import shutil
import os
import time
from tkinter import *
import tkinter.filedialog as fdialog


class MainClass():

    def __init__(self, master):
        self.parent=master
        self.gui()


    def gui(self):
        self.Source=StringVar()#assigning source to stringvar to keep track of the source selection
        self.Destination=StringVar()#assigning Destination to StringVar to keep track of the destination

        MySource=Entry(root, textvariable=self.Source)#the text field that will show the file path of the source folder
        browse1=Button(root, text="Browse",command=lambda: Source(self))#creating our browse button to call up our function to look for the filepath
        MyDestination=Entry(root, textvariable=self.Destination)#the text field that will show the destination file path
        browse2=Button(root,text="Browse",command=lambda: Dest(self))#the second browse button to call up the second function to grab the file path
        buttonCopy=Button(root, text="  Copy  ", command= self.copyy)#our third button to copy over the files that fit within our critera
        #this next block is all about the grid geometry for our GUI
        MySource.grid(row=2, column=2, columnspan=2)
        browse1.grid(row=2, column=5, sticky=E)
        MyDestination.grid(row=4, column=2, columnspan=2)
        browse2.grid(row=4, column=5,sticky=E)
        buttonCopy.grid(row=11, column=3)

    SECONDS_IN_DAY = 24 * 60 * 60#sets the foundation to create a function
    now = time.time()#that will look through the files and only copy the ones 
    before = now - SECONDS_IN_DAY#that have been modified in the last 24 hrs

    def last_mod_time(fname):#here we are defining the function that will see the last
        return os.path.getmtime(fname)#time the file was modified.

    def copyy(self):#this function will use the last_modified function and then use 
        source_file = self.Source.get()#an if statement to use the parameters that will
        dest_fold = self.Destination.get()#copy the files that were modified in the last 24 hrs and that they are .txt files
        if (source_file.endswith(".txt") and last_mod_time(source_file) > before):
            shutil.copy(source_file, dest_fold)
            print("copy succesful")

def Source(self):
    source_file = self.Source.set(fdialog.askdirectory())

def Dest(self):
    destination = self.Destination.set(fdialog.askdirectory())
        

if __name__ == '__main__':
    root = Tk()
    App = MainClass(root)
    root.geometry("300x150")
    root.mainloop()
