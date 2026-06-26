from random import randint
n=randint(1,3)
r=input("enter rock, paper or scissors ")
if(n==1):
    print("rock")
if(n==2):
    print("scissors")
if(n==3):
    print("paper")
if(n==1 and r=="paper"):
    print("you win")
if(n==2 and r=="rock"):
    print("you win")
if(n==3 and r=="scissors"):
    print("you win")
if(n==1 and r=="rock"):
    print("tie")
if(n==2 and r=="scissors"):
    print("tie")
if(n==3 and r=="paper"):
    print("tie")
if(n==1 and r=="scissors"):
    print("you lose")
if(n==2 and r=="paper"):
    print("you lose")
if(n==3 and r=="rock"):
    print("you lose")