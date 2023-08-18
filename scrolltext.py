import tkinter as tk
# from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText


# turtle= tk.Tk()

# turtle.title("Scroll Text")

# st = ScrolledText(turtle, width=50, height=10)
# st.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

# turtle.mainloop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ScrollText Widget")
        st = ScrolledText(self, width=50, height=10)
        st.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
        
if __name__=='__main__':
    app=App()
    app.mainloop()