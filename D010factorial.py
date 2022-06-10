def rec(n):
    if n==1:
        return 1
    else:
        return n*rec(n-1)

n=int(input("Enter a value:"))
if (n==0):
    print("factorial=1")
elif(n<0):
    print("Factorial cannot be determined")
else:
    print("Factorial=",rec(n))