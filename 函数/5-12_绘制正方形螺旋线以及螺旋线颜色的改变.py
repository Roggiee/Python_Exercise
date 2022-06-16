import turtle

color = ["red", "green", "yellow", "blue"]
def a(x,y,z):

    turtle.pencolor()
    turtle.up()
    turtle.goto(x,y)

    turtle.down()
    turtle.seth(90)
    turtle.fd(3)

    for i in range(99):
        #turtle.color(color[i])
        turtle.fd(i*20)
        turtle.left(90)
        turtle.pencolor(color[i%4])

a(0,0,50)

turtle.done()