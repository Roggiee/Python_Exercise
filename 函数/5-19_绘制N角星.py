import turtle
def stars(side,length,startx,starty,pensizes,mycolor):
    turtle.color(mycolor)
    turtle.pensize(pensizes)
    turtle.penup()
    turtle.goto(startx,starty)
    turtle.pendown()
    for i in range(side):
        turtle.forward(length)
        turtle.right(180-180/side)
    turtle.done
stars(55,300,-150,150,1,"red")
