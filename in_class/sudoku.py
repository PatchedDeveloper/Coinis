from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

m = [[1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9],
     [1,2,3,4,5,6,7,8,9]]

matrix_of_inputs = []

for i in range(10): 
    row_of_inputs = []
    for j in range(9):  
        input_ = ttk.Entry(frm, width=4)  
        input_.grid(column=j, row=i)
        input_.insert(0, m[i][j])
        row_of_inputs.append(input_)
    matrix_of_inputs.append(row_of_inputs)

print(m)

root.mainloop()
