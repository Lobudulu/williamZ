s=0
print("points",s)
print("How many flushed lights are in this room?")
n=input("enter number")
if(n=="42"):
    print("correct")
    s=s+1
    print("points",s)
else:
    print("incorrect(answer:42)")
    s=s+0
    print(s)
print("How many exit signs are in this room")
m=input("enter number")
if(m==4):
    print("correct")
    s=s+1
    print("points",s)
else:
    print("incorrect(answer:4)")
    s=s+0
    print("points",s)
print("How many cameras are in this room")
q=input("enter number")
if(q=="3"):
    print("correct")
    s=s+1
    print("points",s)
else:
    print("incorrect(answer:3)")
    s=s+0
    print("points",s)