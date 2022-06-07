def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("""Operations:
1.Addition
2.Substraction
3.Multiplication
4.Divishion""")

while True:

    ch=input("enter choice:")
    if ch in ('1','2','3','4'):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        if ch == "1":
            print(a,"+",b,"=",add(a,b))
        elif ch == "2":
            print(a,"-",b,"=",sub(a,b))
        elif ch == "3":
            print(a,"*",b,"=",mul(a,b))
        elif ch == "4":
            print(a,"/",b,"=",div(a,b))
   
        nxcal=input("next calculation?(0-no,1-ys):")
        if nxcal == 0:
            break
    else:
         print("invalid option")
