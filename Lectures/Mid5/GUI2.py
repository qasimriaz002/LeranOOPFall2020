from tkinter import *

root = Tk()

topframe = Frame(root, bg="red")
topframe.pack(side = TOP, fill=X, padx = 0, pady = 0, expand=TRUE)
bottomframe = Frame(root, bg="blue")
bottomframe.pack(side = TOP, fill=Y, padx = 0, pady = 0, expand=TRUE)

# button1 = Button(topframe, text="Button 1", fg="red")
# button2 = Button(topframe, text="Button 2", fg="blue")
# button3 = Button(topframe, text="Button 3", fg="green")
# button4 = Button(bottomframe, text="Button 4", fg="purple")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack()

root.mainloop()