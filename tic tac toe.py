board=[]
for i in range(3):
    row=[]
    for g in range(3):
        row.append("◻")
    board.append(row)
for row in board:
    print(row)
s=0
while True:
    x=int(input("enter row number(0,1 or 2)"))
    while x!=0 and x!=1 and x!=2:
        print("You better do a legal move or i might slap you")
        x=int(input("enter row number(0,1 or 2)"))
    g=int(input("enter column number(0,1 or 2)"))
    while g!=0 and g!=1 and g!=2:
        print("You better do a legal move or i might slap you")
        g=int(input("enter column number(0,1 or 2)"))
    while board[x][g]!="◻":
        print("You better do a legal move or i might slap you")
        x=int(input("enter row number(0,1 or 2)"))
        g=int(input("enter column number(0,1 or 2)"))
    board[x][g]="X"
    for row in board:
        print(row)
    if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
        print("X wins")
        break
    if board[1][1]=="X" and board[1][2]=="X" and board[1][0]=="X":
        print("X wins")
        break
    if board[2][1]=="X" and board[2][2]=="X" and board[2][0]=="X":
        print("X wins")
        break
    if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
        print("X wins")
        break
    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print("X wins")
        break
    if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
        print("X wins")
        break
    if board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
        print("X wins")
        break
    if board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
        print("X wins")
        break
    s=s+1
    if(s==9):
        print("tie")
        break
    x=int(input("enter row number(0,1 or 2)"))
    while x!=0 and x!=1 and x!=2:
        print("You better do a legal move or i might slap you")
        x=int(input("enter row number(0,1 or 2)"))
    g=int(input("enter column number(0,1 or 2)"))
    while g!=0 and g!=1 and g!=2:
        print("You better do a legal move or i might slap you")
        g=int(input("enter column number(0,1 or 2)"))
    while board[x][g]!="◻":
        print("You better do a legal move or i might slap you")
        x=int(input("enter row number(0,1 or 2)"))
        g=int(input("enter column number(0,1 or 2)"))
    board[x][g]="O"
    for row in board:
        print(row)
    if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        print("O wins")
        break
    if board[1][1]=="O" and board[1][2]=="O" and board[1][0]=="O":
        print("O wins")
        break
    if board[2][1]=="O" and board[2][2]=="O" and board[2][0]=="O":
        print("O wins")
        break
    if board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
        print("O wins")
        break
    if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print("O wins")
        break
    if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
        print("O wins")
        break
    if board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
        print("O wins")
        break
    if board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
        print("O wins")
        break
    s=s+1
    if(s==9):
        print("tie")
        break