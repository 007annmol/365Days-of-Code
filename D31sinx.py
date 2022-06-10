from math import factorial


x=int(input("Enter a value:"))
n=int(input("Enter range:"))
si=0
tsum=0
for i in range(1,n+1,2):
    val=(x**i)/factorial(i)

    if(si==0):
        tsum +=val
        si=1
    else:
        tsum -=val
        si=0

print("Result:",tsum)
