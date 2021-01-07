from tkinter import *
import tkinter.messagebox
root=Tk()
tkinter.messagebox.showinfo("window title","monkeys can live upto 300 year")
answer=tkinter.messagebox.askquestion("q1","are traveled abroad?")
if answer=='yes':
    print("quarentene")
else:
    print("al coll....")
root.mainloop()