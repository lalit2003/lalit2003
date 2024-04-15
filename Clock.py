from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("CLOCK")

def time():
    String = strftime('%H:%M:%S %p')
    label.config(text=String)
    label.after(1000,time)

label= Label(root,font=("DS-DIGIB.TTF",80),background="Black",foreground="Cyan")
label.pack(anchor='center')
time()


mainloop()