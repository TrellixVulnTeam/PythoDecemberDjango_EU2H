#creating dropdown
from tkinter import *

def do_nothing():
    print("ok ok i.......")


root=Tk()
menu=Menu(root)
root.config(menu=menu)

submenu=Menu(menu)
#dro down is cascade
menu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="new project",command=do_nothing)
submenu.add_command(label="new",command=do_nothing)
submenu.add_separator()#line to separate one group of item
submenu.add_command(label="exit",command=do_nothing)

editmenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="redo",command=do_nothing)


root.mainloop()