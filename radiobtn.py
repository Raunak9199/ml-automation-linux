from tkinter import *
from tkinter.ttk import *

root = Tk()

root.geometry('400x400')

root.title('Radio Button')

selected = IntVar()

rad1 = Radiobutton(root,text='First',value=1, variable=selected)
rad2 = Radiobutton(root,text='Second',value=2,variable=selected)  
rad3 = Radiobutton(root,text='Three',value=3,variable=selected)  
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)

def clicked():
    print(selected.get())
btn = Button(root,text='Click',command=clicked)
btn.grid(column=0, row=1)
root.mainloop()