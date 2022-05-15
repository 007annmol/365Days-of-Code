n=int(input("Enter a binary value:"))
l= len(str(n))
sum=0
for i in n:
    if(i==1):
        sum=pow(2,len)+sum
        len=len-1

print("Decimal:",sum)