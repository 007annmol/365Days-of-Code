import turtle as t
for i in range (50,150):
    t.circle(i)
    t.color("green")
    t.right(160)
    if i%2==0:
        t.left(20)
        t.color("red")
    t.speed(15)
    
