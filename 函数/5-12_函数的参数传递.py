import turtle
def bstar(x,y,z):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor("red")
    for i in range(5):
        turtle.forward(z)
        turtle.left(144)
    turtle.end_fill()
bstar(-80,80,200)
bstar(150,60,150)
turtle.done()