from tkinter import *
from tkinter import Entry

root = Tk()

topframe = Frame(root)
topframe.pack(side = TOP, fill=BOTH, padx = 0, pady = 0, expand=TRUE)
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM, fill=BOTH, padx = 0, pady = 0, expand=TRUE)
lbl_1 = Label(topframe, text="Enter User Name")
lbl_2 = Label(topframe, text="Enter Password")

etext_1 = Entry(topframe)
etext_2 = Entry(topframe)
Btn_login = Button(bottomframe, text = "Login", bg = "white")

etext_2.pack(side=BOTTOM)
lbl_2.pack(side=BOTTOM)
etext_1.pack(side=BOTTOM)
lbl_1.pack(side=BOTTOM)
Btn_login.pack(side=TOP)
root.mainloop()