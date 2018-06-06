from tkinter import *
from tkinter import ttk


def placeposition(event=None):
	print(event.x,event.y)
	ResisterIcon.configure(x=event.x,y=event.y)


GUI = Tk()
GUI.geometry('1200x700')
GUI.bind('<Button-1>', placeposition)

Frame1 = Frame(GUI, height=100)
Frame1.grid(row=0,column=0)

Resister = ttk.Button(Frame1, text='Resister', command=placeposition)
Resister.grid(row=0,column=0)

DrawFrame = Frame(GUI, height=500,borderwidth=4)
DrawFrame.grid(row=1,column=0)

IR = PhotoImage(file='resister.png')
IR.subsample(1,1)
ResisterIcon = Label(GUI,image=IR)
ResisterIcon.place(x=100,y=100)




GUI.mainloop()