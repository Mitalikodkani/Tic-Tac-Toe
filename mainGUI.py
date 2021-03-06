from faulthandler import disable
from itertools import count
from tkinter import *
from tkinter import messagebox

from numpy import true_divide
from pygame import WINDOWENTER

root = Tk()
root.title('Tic-Tac-Toe')

#X starts, so... true
def start(a):
    global clicked
    clicked = a
count = 0
winner=False

#Buttons
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, chooseBtnX, chooseBtnO
    global clicked, count
    clicked=True
    count= 0
    if count==0:
        chooseBtnX = Button(root, text=" X ", font=("Helvetica", 20), height=2, width=6, bg="red", command=lambda: start(True))
        chooseBtnO = Button(root, text=" O ", font=("Helvetica", 20), height=2, width=6, bg="green", command=lambda: start(False))

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    #Grid our buttons to the screen
    chooseBtnX.grid(row=0, column=0)
    chooseBtnO.grid(row=0, column=1)

    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)

    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)

    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)

#disable all buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game",command = reset)

#winner
def winnerX(a,b,c):
    global winner
    winner = False
    a.config(bg="red")
    b.config(bg="red")
    c.config(bg="red")
    winner = True
    messagebox.showinfo("Tic Tac Toe","Congratulations! X Wins!!!")
    disable_all_buttons()

def winnerO(a,b,c):
    global winner
    winner = False
    a.config(bg="green")
    b.config(bg="green")
    c.config(bg="green")
    winner = True
    messagebox.showinfo("Tic Tac Toe","Congratulations! O Wins!!!")
    disable_all_buttons()

#Check to see if someone won
def checkifwon():

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        winnerX(b1,b2,b3)
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        winnerX(b4,b5,b6)
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        winnerX(b7,b8,b9)
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        winnerX(b1,b4,b7)
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        winnerX(b2,b5,b8)
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        winnerX(b3,b6,b9)
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        winnerX(b1,b5,b9)
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        winnerX(b3,b5,b7)
    
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        winnerO(b1,b2,b3)
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        winnerO(b4,b5,b6)
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        winnerO(b7,b8,b9)
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        winnerO(b1,b4,b7)
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        winnerO(b2,b5,b8)
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        winnerO(b3,b6,b9)
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        winnerO(b1,b5,b9)
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        winnerO(b3,b5,b7)
    
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie! \n No wins ")
    
    if count>0:
        chooseBtnX.config(state=DISABLED)
        chooseBtnO.config(state=DISABLED)

#Button clicked function
def b_click(b):
    global clicked, count, winner
    winner = False
    
    '''if x is clicking on a button whose text is empty
    elif o is clicking on a button whose text is empty'''
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count = count+1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        count = count +1
        clicked = True
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! Click properly")





reset()
root.mainloop()

