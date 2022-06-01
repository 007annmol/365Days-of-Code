import turtle as t

s=t.Screen()
c=['#9400d3','#4b0082','#0000ff','#00ff00','#ffff00','#ff7f00','#ff0000']
s.bgcolor("black")

t.penup()
t.pendown()
t.speed(22)

for i in range (200):
    t.pencolor(c[i%7])
    t.fillcolor(c[i%7])
    t.begin_fill()
    for j in range (3):
        t.left(120)
        t.fd(i*0.7)
    t.end_fill()
    t.penup()
    t.fd(i*2)
    t.left(53)
    t.pendown()

t.done()