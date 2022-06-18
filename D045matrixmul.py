r1=int(input("enter no. of row:"))
c1=int(input("Enter no. of coloum:"))

r2=int(input("enter no. of row:"))
c2=int(input("Enter no. of coloum:"))

if r2==c1:
    a=[]
    b=[]
    sum=[]

    #matrix a
    print("Enter elements in matrix A:\n")
    for i in range (r1):
        temp=[]
        temp1=[]
        for j in range (c1):
            temp+=[int(input())]
        a+=[temp]

    #matrix b
    print("Enter elements in matrix B:\n")
    for i in range (r2):
        temp1=[]
        for j in range (c2):
            temp1+=[int(input())]
        b+=[temp1]


    #create a 0 initialized sum list
    for i in range (r1):
        c=[]
        for j in range(c2):
            c+=[0]
        sum+=[c]
    print(sum)
    
    print("A:",a)
    print("B:",b)
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                sum[i][j]=a[i][k]*b[k][j]
    
    print("Sum:",sum)
        
else:
    print("Multiplication not possibel")



