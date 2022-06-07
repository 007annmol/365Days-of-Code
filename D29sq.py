import turtle as t

screen =t.Screen()
t.shape('square')
t.color('aqua')
for s in range(10):
    for i in range(4):
        t.left(90)
        t,t.forward(s*20)

t.bye()