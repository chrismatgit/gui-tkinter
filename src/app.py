from tkinter import *

# create an empty window
window = Tk()
# function to convert a km to miles
def km_to_miles():
    # insert the value to the text widget
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

# create a button
b1 = Button(window, text='Execute', command=km_to_miles) # command take a function as argument
# display the button
b1.grid(row=0,column=0)

# create an entry
e1_value = StringVar() # value holder for string value
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1) 

# create a widget(textarea) area
t1 = Text(window, width=20, height=1)
t1.grid(row=0,column=2)
# make sure wont close in a short time
window.mainloop()