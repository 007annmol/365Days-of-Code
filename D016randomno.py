import random
f=open("num.txt","w")
for i in range (0,100):
    r=random.randint(1,100)
    f.write(str(r)+'\n')
    print(r)

f.close()   