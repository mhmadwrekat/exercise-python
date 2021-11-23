#from tkinter import *
from tkinter import ttk
import time
from tkinter import Label
from tkinter import Tk
root = Tk

root.title('Digital')
clock = Label(root, font = ('Calivri', 90),background = 'black', foreground = 'white' )
clock.pack()

root.mainloop()

"""
root.title = 'Digital'
clock = Label(root, font = ('Calivri', 90),background = 'black', foreground = 'white' )

def get_time() :
    string = time.strftime('%H:%M:%S %P')
    clock.config(text = string)
    clock.after(200, get_time)
clock = Label(root.title, font = ('Calivri', 90),background = 'black', foreground = 'white' )

#tk.Tcl().eval('info patchlevel')
#tk._test()

root.title("Digital")
clock = Label(root.title, font = ('Calivri', 90),background = 'black', foreground = 'white' )

root.title("Digital")
clock = Label(root.title, font = ('Calivri', 90),background = 'black', foreground = 'white' )

def get_time() :
    string = time.strftime('%H:%M:%S %P')
    clock.config(text = string)
    clock.after(200, get_time)

clock.pack()
get_time()

root.mainloop()

from tkinter import Label
import time
import sys
from tkinter.ttk import *

def view():
    print('\n|------------------------------------------|')

rot = tk.Tk()
rot.title("Digital Clock")









#if __name__ =="__main__":


clock.pack()
get_time()

rot.mainloop()
"""
