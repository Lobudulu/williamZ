def square(n):
    print(n*n)
def subtract(n,o):
    print(n-o)
def division(n,o):
    print(n/o)
def add(n,o):
    print(n+o)
def multiply(n,o):
    print(n*o)
n=int(input("What is your first number "))
s=input("multiplecation, addition, division, subtraction, or squaring ")
if(s=="squaring"or"**"):
    square(n)
else:
    o=int(input("What is the other number "))
if(s=="-"or (s=="subtraction")):
    subtract(n,o)
if(s=="/"or(s=="divsion")):
    division(n,o)
if(s=="+"or(s=="addition")):
    add(n,o)
if(s=="*"or(s=="multiplecation")):
    multiply(n,o)