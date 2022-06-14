x=int(input("enter x-coordinate:"))
y=int(input("enter y-coordinate:"))

if(x>0):
    if(y>0):
        print("1st quadrent")
    elif y<0:
        print("4th quadrent")
elif x<0:
    if(y>0):
        print("2nd quadrent")
    elif y<0:
        print("43rd quadrent")
elif x==0 & y==0:
    print("origin")
elif x!=0 & y==0:
    print("x-axis")
else:
    print("y-axis")