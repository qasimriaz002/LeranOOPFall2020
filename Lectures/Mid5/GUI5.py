from tkinter import *

root = Tk()
root.state("zoomed")
frame_left = Frame(root, bg = 'Pink', width = 400)
frame_right = Frame(root, bg = 'Brown')
frame_extreme_right = Frame(root, bg = 'Pink', width = 50)
frame_top = Frame(frame_right, bg = 'Pink', height=50)
frame_upper = Frame(frame_right, bg='Red')
frame_lower = Frame(frame_right, bg='Green')
frame_bottom = Frame(frame_right, bg = 'Pink', height=50)

frame_left.pack(side=LEFT, fill=BOTH)
frame_right.pack(side=LEFT, fill=BOTH, expand=1)
frame_extreme_right.pack(side=LEFT, fill=BOTH)
frame_top.pack(side = TOP, fill=X)
frame_upper.pack(side=TOP, fill=BOTH, expand = 1)
frame_lower.pack(side=TOP, fill= BOTH, expand = 1)
frame_bottom.pack(side=BOTTOM, fill=X)



# frame_upperContainer = Frame(root, bg='red')
# frame_lowerContainer = Frame(root, bg='blue')
# frame_bottomButtonsContainer = Frame(root, bg='green')

# btn_1 = Button(frame_upper, text ="Button - 1")
# btn_2 = Button(frame_upper, text ="Button - 2")
# btn_3 = Button(frame_lower, text ="Button - 3")
# btn_4 = Button(frame_bottom,text = "Button - 4")
# btn_5 = Button(frame_bottom,text = "Button - 5")



# btn_1.pack()
# btn_2.pack()
# btn_3.pack()
# btn_4.pack()
# btn_5.pack()


#
# frame_upperContainer.pack(side=TOP, fill=BOTH, expand=1)
# frame_upperContainer.pack_propagate(0)
# frame_lowerContainer.pack(side=TOP, fill=BOTH, expand=1)
# frame_lowerContainer.pack_propagate(0)
# frame_bottomButtonsContainer.pack(side=BOTTOM, fill=X, expand=1)


root.mainloop()