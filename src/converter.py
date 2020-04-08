from tkinter import *

# create an empty window
window = Tk()
# function to convert from kg to gram, pound and ounce
def convert_from_kg():
    # insert the value to the texts widgets
    grams = float(e2.get())*1000 # convert kg to grams
    t1.delete("1.0", END) # empty the input field
    t1.insert(END, grams)

    pounds = float(e2.get())*2.20462 # convert kg to pounds
    t2.delete("1.0", END) # empty the input field
    t2.insert(END, pounds)

    ounces = float(e2.get())*35.274 # convert kg to ounces
    t3.delete("1.0", END) # empty the input field
    t3.insert(END, ounces)

# Design section
e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)

b1=Button(window,text="Convert",command=convert_from_kg)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)
# make sure wont close in a short time
window.mainloop()