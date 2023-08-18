import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.title("Checkbox")
root.geometry('400x400')

l= tk.Label(root, bg='white', width=50, height=50, text='Empty')
l.pack()

def printSelection():
    if (var1.get()==1)&(var2.get()==0):
        l.config(text='I love python')
    elif (var1.get()==0)&(var2.get()==1):
        l.config(text='I love c++')
    elif (var1.get()==0)&(var2.get()==0):
        l.config(text='I do not love anything')
    else: 
        l.config("I love both")

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(root,text='Python', variable=var1, onvalue=1, offvalue=0, command=printSelection)
c1.pack()
c2 = tk.Checkbutton(root,text='C++', variable=var2, onvalue=1, offvalue=0, command=printSelection)
c2.pack()

root.mainloop()