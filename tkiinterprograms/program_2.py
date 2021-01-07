#organizing layout
from tkinter import *
root=Tk()
#frame is a invisible screen which is a layout
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
button1=Button(topFrame,text="Button1",fg="red")
button2=Button(topFrame,text="Button2",fg="green")

button3=Button(topFrame,text="Button3",fg="blue")

button4=Button(bottomFrame,text="Button4",fg="cyan")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop()