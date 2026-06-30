def animal(moose,pig):
    for i in range(3):
        if board[moose][i]==pig and board[moose][i+1]==pig and board[moose][i+2]==pig and board[moose][i+3]==pig:
            print(pig,"won")
            return True    
def camel(donkey,cow):
    for g in range(3):
        if board[g][donkey]==cow and board[g+1][donkey]==cow and board[g+2][donkey]==cow and board[g+3][donkey]==cow:
            print(cow,"won")
            return True
def b(a,r,b):
    for r in range(3):
        if board[r-1][a-1]==b and board[r-2][a-2]==b and board[r-3][a-3]==b and board[r-4][a-4]==b:
            print(b,"won")
            return True
def a(z,m,n):
    for m in range(3):
        if board[m-1][z+1]==n and board[m-2][z+2]==n and board[m-3][z+3]==n and board[m-4][z+4]==n:
            print(n,"won")
            return True
print("rules:")
print("if you choose to put your tile in a filled column then your turn gets skipped")
print("Don't do anything bad or you will get a slap")
board=[]
r=True
for i in range(6):
    row=[]
    for g in range(7):
        row.append('  ')
    board.append(row)
for row in board:
    print(row)
s=[5,5,5,5,5,5,5,5]
while r==True:
    x=int(input("enter column number (1,2,3,4,5,6,or 0)"))
    if x!=1 and x!=2 and x!=3 and x!=4 and x!=0 and x!=5 and x!=6:
        x=int(input("enter column number (1,2,3,4,5,6,or 0)"))
        print("you can't do that")
    if x==0:
        board[s[1]][x]="🟡" 
        s[1]=s[1]-1
    if x==1:
        board[s[2]][x]="🟡" 
        s[2]=s[2]-1
    if x==2:
        board[s[3]][x]="🟡" 
        s[3]=s[3]-1
    if x==3:
        board[s[4]][x]="🟡" 
        s[4]=s[4]-1
    if x==4:
        board[s[5]][x]="🟡" 
        s[5]=s[5]-1
    if x==5:
        board[s[6]][x]="🟡" 
        s[6]=s[6]-1
    if x==6:
        board[s[7]][x]="🟡" 
        s[7]=s[7]-1

    for row in board:
        print(row)
    for i in range(6):
        #animal(i,"🟡")
        if animal (i,"🟡")==True:
            break
    for i in range(7):
        if camel(i,"🟡")==True:
            break
    for i in range(3):
        for g in range(3):
            if tgghbhhhgvffggg(i,g,"🟡")==True:
                break
    for i in range(3):
        for g in range(3):
            if ffjdkfjkdjfkdjfkdjfkdjfkjdkfjkdjfkdjkfjdkfkdfkfdjfdkfjkdjfkdjfkdjfkdkjfkdjfk(i,g,"🟡")==True:
                break
    x=int(input("enter column number (1,2,3,4,5,6,or 0)"))
    if x!=1 and x!=2 and x!=3 and x!=4 and x!=0 and x!=5 and x!=6:
        x=int(input("enter column number (1,2,3,4,5,6,or 0)"))
        print("you can't do that")
    if x==0:
        board[s[1]][x]="🔴" 
        s[1]=s[1]-1
    if x==1:
        board[s[2]][x]="🔴" 
        s[2]=s[2]-1
    if x==2:
        board[s[3]][x]="🔴" 
        s[3]=s[3]-1
    if x==3:
        board[s[4]][x]="🔴" 
        s[4]=s[4]-1
    if x==4:
        board[s[5]][x]="🔴" 
        s[5]=s[5]-1
    if x==5:
        board[s[6]][x]="🔴" 
        s[6]=s[6]-1
    if x==6:
        board[s[7]][x]="🔴" 
        s[7]=s[7]-1
    for row in board:
        print(row)
    for i in range(6):
        #animal(i,"🔴")
        if animal (i,"🔴")==True:
            r=False
    for i in range(7):
        if camel(i,"🔴")==True:
            r=False
    for i in range(4):
        for g in range(4):
            #b(i,g,"🔴")
            if b(i,g,"🔴")==True:
                r=False
    for i in range(3):
        for g in range(3):
            if tgghbhhhgvffggg(i,g,"🔴")==True:
                break
    for i in range(3):
        for g in range(3):
            if ffjdkfjkdjfkdjfkdjfkdjfkjdkfjkdjfkdjkfjdkfkdfkfdjfdkfjkdjfkdjfkdjfkdkjfkdjfk(i,g,"🔴")==True:
                break