from tkinter import *

window = Tk()
window.geometry('500x400')

window.title("Hello")

lbl= Label(window, text='Hello',font=("Arial Bold",30))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1,row=0)

def clicked():
    res="Welcome to "+txt.get()
    lbl.configure(text=res)
    
btn=Button(window,text="Click", bg="green", fg="black", command=clicked)
btn.grid(column=2,row=0)

window.mainloop()