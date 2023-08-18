from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('500x400')

window.title("ComboBox")

combo = Combobox(window)

combo['values'] = (1,2,3,4,5,"Hello")
combo.current(2)
combo.grid(column=0,row=0)

lbl = Label(window, text="Select a value")
lbl.grid(column=0, row=1)

def clicked():
    # print(combo.get())
    lbl.configure(text=combo.get())

btn = Button(text="Click", command=clicked)
btn.grid(column=1,row=0)

window.mainloop()