row=int(input("enter no. of row:"))
col=int(input("Enter no. of coloum:"))

a=[]
b=[]
c=[]
print("Enter elements in matrix A:\n")
for i in range (row):
    temp=[]
    temp1=[]
    for j in range (col):
        a+=[[int(input())]]
        temp1+=[0]
    c+=[temp1]

print("Enter elements in matrix B:\n")
for i in range (row):
    temp1=[]
    for j in range (col):
        temp1+=[int(input())]
    b+=[temp1]

print("A:",a)
print("B:",b)

for i in range (row):
    print("*")
    for j in range(col):
        c[i][j]=a[i][j]+b[i][j]
        
print(c)
