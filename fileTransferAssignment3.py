import shutil
import os
import time
from tkinter import *
import tkinter.filedialog as fdialog
from datetime import datetime, timedelta

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
    now = datetime.now()#that will look through the files and only copy the ones 
    before = now - timedelta(hours=24)#that have been modified in the last 24 hrs

    def last_mod_time(fname):#here we are defining the function that will see the last
        mtime = os.path.getmtime(fname)
        modTime = datetime.fromtimestamp(mtime)
        return modTime#time the file was modified.

    def copyy(self):
        #gets the path to the source folder
        source_file = self.Source.get()
        #gets the path to the destination folder
        dest_fold = self.Destination.get()

        #gets the list of files in the source path
        fileList = os.listdir(source_file)

        for file in fileList:
            #gets the absolute path to the file in the source folder
            absolutePath = os.path.join(source_file, file)
            
            if (absolutePath.endswith(".txt") and MainClass.last_mod_time(absolutePath) > MainClass.before):
                shutil.copy(absolutePath, dest_fold)
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
