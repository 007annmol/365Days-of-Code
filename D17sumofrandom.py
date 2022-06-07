f=open("num.txt","r")
sum=0
n=f.read()
for i in n:
    print(i)
    if i in ('0','1','2','3','4','5','6','7','8','9'):
        sum=sum+int(i)
   
print("sum=",sum)