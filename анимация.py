import turtle
t = turtle.Pen()
turtle.speed(10)
turtle.delay(0)
for x in range(360):
    t.width(x/100+1)
    t.forward(x)
    t.right(59)



turtle.exitonclick()



