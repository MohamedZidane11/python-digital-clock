from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Welou Digital Clock')
root.geometry('350x70+10+10')
root.iconbitmap('Jommans-Mushroom-Clock.ico')

def time():
    format = strftime('%H:%M:%S - %p')
    properties.config(text=format)
    properties.after(1000,time)

##3498db
properties = Label(root, font=('ds-digital',50),background='#2d3436',foreground='#3498db')
properties.pack(anchor='center', fill='both')

time()
mainloop()