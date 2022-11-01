import os
import time
from pathlib import Path
from colorama import Fore # might want to use 'rich'
from tqdm import tqdm
from tkinter import filedialog
from tkinter import *
import sys

BG_COLOR = '#395778'
FG_COLOR = 'white'

def browse_source():
    global source_path
    filename = filedialog.askdirectory()
    source_path.set(filename)


def browse_destination():
    global destination_path
    filename = filedialog.askdirectory()
    destination_path.set(filename)

def execute():
    root.destroy()

root = Tk()
root.geometry("400x200")
# root.iconbitmap('week12/calc.ico')
Frame(root).master.title("File Mover Path Specifier")

source_path = StringVar()
destination_path = StringVar()

lbS = Label(root,textvariable=source_path)
lbS.pack(fill=X)
btnS = Button(text="Enter Source Directory", command=browse_source, bg=BG_COLOR, fg=FG_COLOR, font=12)
btnS.pack(fill=X)
lbD = Label(root,textvariable=destination_path)
lbD.pack(fill=X)
btnD = Button(text="Enter Destination Directory", command=browse_destination, bg=BG_COLOR, fg=FG_COLOR, font=12)
btnD.pack(fill=X)
btnX = Button(text="Execute", command=execute, bg=BG_COLOR, fg=FG_COLOR, font=12)
btnX.pack(fill=X, pady=20)

mainloop()

# NOTE: This is where first window is destroyed and new one started | values are accessed 

print(source_path.get())
print(destination_path.get())

def close():
    root.destroy()

root = Tk()
root.geometry("700x400")
# root.iconbitmap('week12/calc.ico')
Frame(root).master.title("File Mover Execution")
log_box = Text(root)
log_box.pack(fill=X)

class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''
    def __init__(self,text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.insert("end", str)
    def flush(self):
        pass

# To start redirecting stdout:
sys.stdout = StdoutRedirector( log_box )

# WARNING:
# To stop redirecting stdout:
# sys.stdout = sys.__stdout__

print("test1")
print("test2")


mainloop()