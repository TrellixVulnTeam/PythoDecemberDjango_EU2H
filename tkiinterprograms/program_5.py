#binding function to lay out

from tkinter import *
root=Tk()

def print_name():
    print("event binding")
button_1=Button(root,text="print my name",command=print_name)
button_1.pack()
root.mainloop()