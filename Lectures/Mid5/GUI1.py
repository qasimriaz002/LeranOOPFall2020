from tkinter import *

root = Tk()

lbl_1 = Label(text="Are you sure to select this option")
btn_1 = Button(text="Okay Select", bg = "Red", fg="white")
btn_2 = Button(text="Cancel")



lbl_1.pack(side=TOP)
btn_1.pack(side=LEFT)
btn_2.pack(side=RIGHT)



root.mainloop()
