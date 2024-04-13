from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

input_1_1 = ttk.Entry(frm, width=50)
input_1_1.grid(column=0, row=0)
input_1_1 = ttk.Entry(frm, width=50)
input_1_1.grid(column=0, row=0)



def print_input_value_to_console ():
    print(input.get())

label_helloWorld = ttk.Label(frm, text="Hello user!").grid(column=0, row=0)


input.insert(0, "Type here ...")
input.grid(column=0, row=1)

button_print = ttk.Button(frm, text="Print Text", command=print_input_value_to_console).grid(column=0, row=2)
quite_btn = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)


root.mainloop()