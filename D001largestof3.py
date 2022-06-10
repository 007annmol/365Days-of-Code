a=int(input("Enter a value"))
b=int(input("Enter a value"))
c=int(input("Enter a value"))
if(a>b and a>c):
    print("the largest number is",a)
elif(b>a and b>c):
    print("The largest number:",b)
else:
    print("The largest number:",c)