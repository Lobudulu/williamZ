r=[]
n=int(input("how many items "))
for i in range(n):
    x=input("enter item ")
    r.append(x)
    print("shopping list:")
    for item in r:
        print(item)