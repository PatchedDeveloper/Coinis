import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk

sudoku_page = requests.get('https://west.websudoku.com/')
soup = BeautifulSoup(sudoku_page.content, 'html.parser')
print(soup)
board = [[0 for element in range(9)] for row in range(9)]
for i in range(9):
    for j in range(9):
        cell_id = f"f{i}{j}"
        cell = soup.find(id=cell_id)
        if cell and "readonly" in cell.attrs:
            board[i][j] = int(cell['value'])
        else:
            board[i][j] = 0        

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
matrix_of_inputs = []

def on_key_release(event, row , column):
    print(row , column)
    print(event.widget.get())
    board[row][column] = int(event.widget.get())

for i in range(0,9): 
    row_of_inputs = []
    for j in range(0,9):  
        input = ttk.Entry(frm, width=4)  
        input.grid(column=j, row=i)
        input.bind('<KeyRelease>',lambda event,row=i,column=j : on_key_release(event,row,column))
        if not board[i][j] == 0:
            input.insert(0, board[i][j])
        row_of_inputs.append(input)
    matrix_of_inputs.append(row_of_inputs)

root.mainloop()
