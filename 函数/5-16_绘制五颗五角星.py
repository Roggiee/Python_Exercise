import turtle
def huax(x,y,z):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor("yellow")

    for i in range(5):
        turtle.forward(z)
        turtle.left(144)

    turtle.end_fill()

turtle.color("yellow")
huax(-250,230,100)
huax(-31,290,60)
huax(-30,181,60)
huax(-100,81,60)
huax(-210,65,60)
turtle.screensize(bg="red")
turtle.done()
