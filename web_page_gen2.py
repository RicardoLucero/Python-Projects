import tkinter as tk
from tkinter import *
import webbrowser#we import  webbrowser to allow us to make the HTML file
#and write,save, and open the file in a web browser and with certain parameters
#we can have the file open in certain browsers and in a new tab

root = Tk()
root.geometry("450x300")#defines the size of our gui window
root.title("Body Text Insert webpage")

def clear_textbox():#our button's function to clear the text box
    text_box.delete(1.0, 'end')#the parameters are from where to delete
    #the first parameter is where to start and the second is where to end

def create_page():#this function will use the get method to collect all the text
    Input = text_box.get(1.0, 'end')#and save it in a variable for use later
    f = open("clientwebpage.html","w")#we then check to open an html file for our client if not found then it is created and the 'w' means we will overwrite the file when we write our file
    f.write(Input)#we now use our variable Input and write it in the file
    f.close()#we finish by closing the file and letting the system know we are done writing in the file
    f= open("clientwebpage.html", "r")#now we open the file but only in read mode
    print(f.read())
    webbrowser.register('chrome',None)#we are telling the system that we want to open the file in google chrome if available
    url= "clientwebpage.html"#we tell the browser the url we want the browser to go to
    webbrowser.open_new_tab(url)#we tell the browser to open the url in a new tab


text_box = Text(root, height=15, width=35)#creatign the text boc
btnclr = Button(root, text='Clear', width=12, height=1, command=clear_textbox)#our cancel button
btnsubmit = Button(root, text='Submit', width=12, height=1,command=create_page)#our submit and create button

text_box.grid(row=1, column=3,padx=(60,15), sticky=EW)#we use the grid geometry method to place our text box and buttons
btnclr.grid(row=2, column=3,padx=(60,15),pady=(15,0), sticky=NW)
btnsubmit.grid(row=2, column=3,padx=(30,15), pady=(15,0), sticky=NE)

mainloop()
