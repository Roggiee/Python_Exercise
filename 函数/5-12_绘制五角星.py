import turtle
def astar():
    turtle.color('red','red')
    turtle.begin_fill()
    for i in range(5):
        turtle.fd(200)
        turtle.rt(144)
    turtle.end_fill()
astar()
turtle.goto(-30,80)
astar()
turtle.done()
