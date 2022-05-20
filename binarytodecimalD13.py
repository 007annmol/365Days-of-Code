n=(input("Enter a binary value:"))
l= len(str(n))
sum=0
for i in n:
    l=l-1
    if(i=="1"):
        sum=pow(2,l)+sum

print("Decimal:",sum)