Step1: from tkinter import *
Step2: make a variable (here, root = Tk()) to use as pointer to tkinter
       - to open a new window use.... root.mainloop() ....at the end
       - to name the window.... root.title('Tic-Tac-Toe') 
Step3: To create buttons
       - There are 9 buttons.... b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
       - These buttons contain the parameters --- master window, text, font, height, width, bg, command
       - In the command parameter we give a function called --- b_click ---
       - We make 9 buttons from b1 to b9

// our next step would be to make grid of these 9 buttons and define function b_click

Step4: Grid our buttons to the screen
       - | 1,1 | 1,2 | 1,3 |
         |-----+-----+-----|
         | 2,1 | 2,2 | 2,3 |
         |-----+-----+-----|
         | 3,1 | 3,2 | 3,3 |
        - Arrange the buttons according to the above grid (row,column)
        - ex:.... b1.grid(row=0, column=0) 

Step5: Function --- b_click
    if clicked == true then X's turn, else O's turn
    if the clicked block is empty then the one whose turn it is will fill the block
    also for every turn we are checking if anyone has won using checkifwon() function

Step6: Function --- checkifwon
    ....
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        winnerX(b1,b2,b3)
    ....
     we are going through each possible way of winning
    - if X wins function winnerX will be called 
      and if O wins function winnerO will be called

Step7: Functions --- winnerX(a,b,c) and winnerO(a,b,c)
    - we make buttons a, b, c red if x wins and green if O wins
    - show message of win using....
        messagebox.showinfo("Tic Tac Toe","Congratulations! O Wins!!!")
    - then disable all the buttons

Step8: Function --- disable_all_buttons()
    - .... b1.config(state=DISABLED) .... is used for all buttons from b1 to b9

Step9: Create a menu to reset the game
    - make a variable.... my_menu = Menu(root)
    - configure the menu in the game window.... root.config(menu=my_menu)

    - create a column on top for the menu.... options_menu = Menu(my_menu, tearoff=False)
    - to add a button called 'options' on the menubar.... my_menu.add_cascade(label="Options", menu=options_menu) 
    - on clicking 'options' we need a dropdown with 'Reset' option.... options_menu.add_command(label="Reset Game",command = reset)

Step10: function --- reset()
    - put all the buttons and grid in the function and call it even while starting the game
         
       