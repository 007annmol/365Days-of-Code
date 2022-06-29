r=int(input("enter no.of rows: "))
k=2*r-2
for i in range(0,r):
    for j in range(0,k):
        print("+",end="")
    k=k-1
    for j in range(0,i+1):
        print("*",end="")
    print("")