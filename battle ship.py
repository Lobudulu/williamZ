from random import randint
def print_the_board(board):
    for row in board:
        print(row)
# print("submarine=🛳️")
# board=[]
# for i in range (10):
#     row=[]
#     for g in range(10):
#         row.append("◻")
#     board.append(row)
# print_the_board(board)
# Aircraft_Carrier=[]
# destroyer=[]
# battle_ship=[]
# Cruiser=[]
# Submarine=[]
# for i in range(3):
#     x=input("Where do you want to put your destroyer? ")
#     letter=x[0]
#     number=int(x[1])
#     if letter=="a":
#         a=0
#     if letter=="b":
#         a=1
#     if letter=="c":
#         a=2
#     if letter=="d":
#         a=3
#     if letter=="e":
#         a=4
#     if letter=="f":
#         a=5
#     if letter=="g":
#         a=6
#     if letter=="h":
#         a=7
#     if letter=="i":
#         a=8
#     if letter=="j":
#         a=9
#     destroyer.append(board[a][number])
#     # print(a)
#     # print(number)
#     board[a][number]="🛥"
#     if board[3][7]=="🛥" and board[0][1]=="🛥" and board[6][3]=="🛥":
#         print("You are disqualified because you cheated")
#         break
# print_the_board(board)
# for i in range(3):
#     r=input("Where do you want to put your Submarine? ")
#     Letter=r[0]
#     Number=int(r[1])
#     if Letter=="a":
#         b=0
#     if Letter=="b":
#         b=1
#     if Letter=="c":
#         b=2
#     if Letter=="d":
#         b=3
#     if Letter=="e":
#         b=4
#     if Letter=="f":
#         b=5
#     if Letter=="g":
#         b=6
#     if Letter=="h":
#         b=7
#     if Letter=="i":
#         b=8
#     if Letter=="j":
#         b=9
#     if board[b][Number]!="◻":
#         print("Because you cheated,you don't get part of the Submarine")
#         break
#     Submarine.append(board[b][Number])
#     board[b][Number]="🛳️"
# print_the_board(board)
# for i in range(4):
#     k=input("Where do you want to put your battleship? ")
#     Letter=k[0]
#     Number=int(k[1])
#     if Letter=="a":
#         c=0
#     if Letter=="b":
#         c=1
#     if Letter=="c":
#         c=2
#     if Letter=="d":
#         c=3
#     if Letter=="e":
#         c=4
#     if Letter=="f":
#         c=5
#     if Letter=="g":
#         c=6
#     if Letter=="h":
#         c=7
#     if Letter=="i":
#         c=8
#     if Letter=="j":
#         c=9
#     battle_ship.append(board[c][number])
#     board[c][number]="🚢"
# print_the_board(board)
# for i in range(5):
#     y=input("Where do you want to put your aircraft carrier? ")
#     other_letter=[k][0]
#     other_number=int([k][1])
#     if other_letter=="a":
#         d=0
#     if other_letter=="b":
#         d=1
#     if other_letter=="c":
#         d=2
#     if other_letter=="d":
#         d=3
#     if other_letter=="e":
#         d=4
#     if other_letter=="f":
#         d=5
#     if other_letter=="g":
#         d=6
#     if other_letter=="h":
#         d=7
#     if other_letter=="i":
#         d=8
#     if other_letter=="j":
#         d=9
#     Aircraft_Carrier.append(board[d][other_number])
#     board[d][other_number]="🛬"
#     print_the_board(board)
# for i in range(3):
#     q=input("Where do you want to put your cruiser? ")
#     lettter=[q][0]
#     nummber=int([q][1])
#     if lettter=="a":
#         e=0
#     if lettter=="b":
#         e=1
#     if lettter=="c":
#         e=2
#     if lettter=="d":
#         e=3
#     if lettter=="e":
#         e=4
#     if lettter=="f":
#         e=5
#     if lettter=="g":
#         e=6
#     if lettter=="h":
#         e=7
#     if lettter=="i":
#         e=8
#     if lettter=="j":
#         e=9
#     Aircraft_Carrier.append(board[e][nummber])
#     board[e][nummber]="🛬"
#     print_the_board(board)
# for i in range(2):
#     v=input("Where do you want to put your cruiser? ")
# lettter=[v][0]
# nummber=int([v][1])
# if lettter=="a":
#     f=0
# if lettter=="b":
#     f=1
# if lettter=="c":
#     f=2
# if lettter=="d":
#     f=3
# if lettter=="e":
#     f=4
# if lettter=="f":
#     f=5
# if lettter=="g":
#     f=6
# if lettter=="h":
#     f=7
# if lettter=="i":
#     f=8
# if lettter=="j":
#     f=9
computers_board=[]
for i in range (10):
    row=[]
    for g in range(10):
        row.append("◻")
    computers_board.append(row)
A=randint(0,9)
j=randint(0,9)
computers_board[A][j]="🛳️"
if A==0:
    Q=randint(0,1)
    if computers_board[0][0]=="🛳️":
        Q=randint(0,2)
    if Q==0:
        computers_board[A+1][j]="🛳️"
        computers_board[A+2][j]="🛳️"
    computers_board[A][j]="🛳️"
    if Q==1:
        computers_board[A][j]
        Z=randint(0,1)
        if Z==1:
            computers_board[A][j+1]="🛳️"
            computers_board[A][j+2]="🛳️"
        if Z==0:
            while True:
                if j-1<0:
                    j=randint(0,9)
                if j-2<0:
                    j=randint(0,9)
                if j>1:
                    break
            computers_board[A][j-1]="🛳️"
            computers_board[A][j-2]="🛳️"
    if Q==2:
        while True:
                if j-1<0:
                    j=randint(0,9)
                if j<2:
                    j=randint(0,9)
                    computers_board[A][j]="🛳️"
                    computers_board[A][j-1]="🛳️"
                    computers_board[A][j+1]="🛳️"
if A==9:
    D=randint(0,1)
    if computers_board[0][0]=="🛳️":
        D=randint(0,2)
    if D==0:
        computers_board[A-1][j]="🛳️"
        computers_board[A-2][j]="🛳️"
    computers_board[A][j]="🛳️"
    if D==1:
        computers_board[A][j]
        Z=randint(0,1)
        if Z==1:
            computers_board[A][j-1]="🛳️"
            computers_board[A][j-2]="🛳️"
        computers_board[A][j]="🛳️"
        if Z==0:
            while True:
                if j<1:
                    j=randint(0,9)
                if j>1:
                    break
            computers_board[A][j-1]="🛳️"
            computers_board[A][j-2]="🛳️"
    if D==2:
        while True:
                if j-1<0:
                    j=randint(0,9)
                if j-2<0:
                    j=randint(0,9)
                    computers_board[A][j]="🛳️"
                    computers_board[A][j-1]="🛳️"
                    computers_board[A][j+1]="🛳️"


M=randint(0,9)
F=randint(0,9)
computers_board[M][F]="🛬"
if M==0:
    Q=randint(0,1)
    if computers_board[0][0]=="🛬":
        Q=randint(0,2)
    if Q==0:
        computers_board[M-1][F]="🛬"
        computers_board[M-2][F]="🛬"
        computers_board[M-3][F]="🛬"
        computers_board[M-4][F]="🛬"
    computers_board[M][F]="🛬"
    if Q==1:
        computers_board[M][F]
        Z=randint(0,1)
        if Z==1:
            computers_board[M][F+1]="🛬"
            computers_board[M][F+2]="🛬"
            computers_board[M][F+3]="🛬"
            computers_board[M][F+4]="🛬"
        if Z==0:
            while True:
                if F-1<0:
                    F=randint(0,9)
                if F-2<0:
                    F=randint(0,9)
                if F-3<0:
                    F=randint(0,9)
                if F-4<0:
                    F=randint(0,9)
                if F>5:
                    break
                else:
                    computers_board[M][F-1]="🛬"
                    computers_board[M][F-2]="🛬"
                    computers_board[M][F-3]="🛬"
                    computers_board[M][F-4]="🛬"
    if Q==2:
        while True:
                if F-1<0:
                    F=randint(0,9)
                if F-2<0:
                    F=randint(0,9)
                if F-3<0:
                    F=randint(0,9)
                if F>4:
                    break
        F=randint(0,9)
        computers_board[M][F]="🛬"
        computers_board[M][F-1]="🛬"
        computers_board[M][F+1]="🛬"
        computers_board[M][F+2]="🛬"
        computers_board[M][F-2]="🛬"
if M==9:
    D=randint(0,1)
    if computers_board[0][0]=="🛬":
        R=randint(0,2)
    if R==0:
        while True:
                if F>5:
                    F=randint(0,9)
                if F>4:
                    break
        computers_board[M-1][F]="🛬"
        computers_board[M-2][F]="🛬"
        computers_board[M-3][F]="🛬"
        computers_board[M-4][F]="🛬"
    if R==1:
        computers_board[M][F]
        Z=randint(0,1)
        if Z==1:
            while True:
                if F-1<0:
                    j=randint(0,9)
                if F-2<0:
                    F=randint(0,9)
                if F>4:
                    break
            computers_board[M][F-1]="🛬"
            computers_board[M][F-2]="🛬"
            computers_board[M][F-3]="🛬"
            computers_board[M][F-4]="🛬"
    if R==2:
        while True:
            if F<5:
                F=randint(0,9)
            if F>4:
                break
        computers_board[M][F-1]="🛬"
        computers_board[M][F-2]="🛬"
        computers_board[M][F-3]="🛬"
        computers_board[M][F-3]="🛬"
    if R==2:
        while True:
            if F<4:
                F=randint(0,9)
            if F>4:
                F=randint(0,9)
    computers_board[M][F]="🛬"
    computers_board[M][F-1]="🛬"
    computers_board[M][F-2]="🛬"
    computers_board[M][F+1]="🛬"
    computers_board[M][F+2]="🛬"
print_the_board(computers_board)