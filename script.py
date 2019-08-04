from tkinter import *

window = Tk()


def km_to_miles():
    miles = float(e1val.get())*1.6
    t1.insert(END, miles)


b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=1)

e1val = StringVar()
e1 = Entry(window, textvariable=e1val)
e1.grid(row=0, column=0)

t1 = Text(window, height=1, width=16)
t1.grid(row=0, column=2)

window.mainloop()