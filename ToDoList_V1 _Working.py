"""
Program: NunezKatrinaM06_Ex1.py
Author: Katrina Nunez
To Do List app Version 1
"""

import tkinter as tk
from tkinter import *
from tkinter.constants import *
from Directory import *
from tkinter import messagebox

#Set up the window
window = Tk()
window.title("To-Do List")
window.resizable(width=False, height=False)
window.geometry("500x450+500+200")

#Frame
appFrame = Frame(window)
appFrame.pack()

#Define functions
def newTask():
    task = listEntry.get()
    if task != "":
        tdTasks.insert(END, task)
        listEntry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def newList ():
    task = listEntry.get()
    if task != "":
        tdList.insert(END, task)
        listEntry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a name for your list.")

def deleteTask():
    tdTasks.delete(ANCHOR)

def deleteList():
    tdList.delete(ANCHOR)

def listTasks(e):
    tdTasks.delete(0, END)
    if tdList.get(ANCHOR) == 'Create documentation':
        for item in createDoc:
            tdTasks.insert(END, item)
    if tdList.get(ANCHOR) == 'Type code':
        for item in typeCode:
            tdTasks.insert(END, item)

listLabel = Label(appFrame, text="Lists")
listLabel.grid(row=0, column=0)

taskLabel = Label(appFrame, text="Tasks")
taskLabel.grid(row=0, column=1)

#List boxes
tdList = Listbox(appFrame)
tdTasks = Listbox(appFrame)
tdList.grid(row=1, column=0)
tdTasks.grid(row=1, column=1, padx=20)

#Sample data
taskList = [
    'Create documentation',
    'Type code',
    'Test code',
    'Validate data'
]
for item in taskList:
    tdList.insert(END, item)

createDoc = [
    'Test',
    'Test2',
    'Test3'
]

typeCode = [
    'Code1',
    'Code2'
]

#Bind the Listbox
tdList.bind("<<ListboxSelect>>", listTasks)

#Create entry
listEntry = Entry(window,
                  width=30
)
listEntry.pack(pady=30)

#Create a frame for buttons
buttonFrame = Frame(window)
buttonFrame.pack(pady=30)

#Create buttons
addListButton = Button(
    buttonFrame,
    text='Add List',
    height=2,
    width=10,
    command=newList
)
addListButton.grid(row=0, column=0)

addTaskButton = Button(
    buttonFrame,
    text='Add Task',
    height=2,
    width=10,
    command=newTask
)
addTaskButton.grid(row=0, column=1)

delListButton = Button(
    buttonFrame,
    text='Delete List',
    height=2,
    width=10,
    command=deleteList
)
delListButton.grid(row=1, column=0)

delTaskButton = Button(
    buttonFrame,
    text='Delete Task',
    height=2,
    width=10,
    command=deleteTask
)
delTaskButton.grid(row=1, column=1)

viewArchiveButton = Button(
    buttonFrame,
    text='View Archived Tasks',
    bg='green',
    padx=20,
    pady=10,
    command=deleteTask
)


window.mainloop()