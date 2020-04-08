from tkinter import *

# create an empty window
window = Tk()

# create a button
b1 = Button(window, text='Execute')
# display the button
b1.grid(row=0,column=0)

# create an entry
e1 = Entry(window)
e1.grid(row=0, column=1)

# create a textarea
t1 = Text(window, width=20, height=1)
t1.grid(row=0,column=2)
# make sure wont close in a short time
window.mainloop()