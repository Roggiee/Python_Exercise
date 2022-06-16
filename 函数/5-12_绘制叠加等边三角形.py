import turtle
def triangle(x,y,z):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    for i in range(3):
        turtle.fd(z)
        turtle.rt(120)
    turtle.seth(60)
triangle(-80,80,100)
turtle.rt(120)
triangle(-80,80,100)
triangle(-80,80,100)
turtle.rt(120)
triangle(20,80,100)
turtle.done()

