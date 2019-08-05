from tkinter import *

window = Tk()


def convert():
    grams = float(input_string.get()) * 1000
    op_gr.insert(END, grams)
    pounds = float(input_string.get()) * 2.20462
    op_lb.insert(END, pounds)
    ounces = float(input_string.get()) * 35.274
    op_oz.insert(END, ounces)


kg_text = Label(window, text="Kg --->", width=20)
kg_text.grid(row=0, column=0)

input_string = StringVar()
value_input = Entry(window, width=20, textvariable=input_string)
value_input.grid(row=0, column=1)

convert_btn = Button(window, text="Convert", command=convert, width=20)
convert_btn.grid(row=0, column=2)

op_gr = Text(window, height=1, width=20)
op_gr.grid(row=1, column=0)

op_lb = Text(window, height=1, width=20)
op_lb.grid(row=1, column=1)

op_oz = Text(window, height=1, width=20)
op_oz.grid(row=1, column=2)

window.mainloop()