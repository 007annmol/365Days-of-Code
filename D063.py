from tkinter import mainloop
import turtle as t
t.bgcolor("black")
t.speed(10)

col=['red','blue','green','white']

for i in range (12):
    t.pencolor(col[i%len(col)])
    for i in range(6):
        t.forward(100)
        t.right(90)
        t.forward (10)
        t.right(90)
        t.backward(10)
        t.right(90)
        t.forward (10)
        t.right(90)
        t.backward(10)
        t.left(60)
    t.left(120)
    t.circle(10,90)

mainloop()