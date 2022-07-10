alp=65
n=int(input("enter the range:"))
for i in range (n):
    for j in range (i):
        print('%c'%(alp+j),end='')
    print()
    
