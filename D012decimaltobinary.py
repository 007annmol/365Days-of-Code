n=int(input("enter a value:"))
b=""
while(n>0):
    d=str(n%2)
    b=d+b
    n=int(n/2)

print("Binary:",b)