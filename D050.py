import turtle as t
t.screensize(canvheight=1000, canvwidth=1000)
t.left(90)
t.speed(500)
t.color("green")
t.width(3)

def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)

tree(100)