from tkinter import *
root=Tk()

def left_click(event):
    print("left")

def middle_click(event):
    print("middle")
def right_click(event):
    print("right")
frame=Frame(root,width=300,height=250)
frame.bind("<Button-1>",left_click)
frame.bind("<Button-2>",middle_click)
frame.bind("<Button-3>",right_click)
frame.pack()
root.mainloop()