import turtle

brilliant_green = "#29cc57"

turtle.shape("turtle")
turtle.fillcolor(brilliant_green)
turtle.pencolor(brilliant_green)

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(180)

# green background
turtle.begin_fill()
turtle.pendown()
for _ in range(4):
    turtle.forward(300)
    turtle.left(90)
turtle.end_fill()

# removing the corners
turtle.fillcolor("white")
turtle.pencolor("white")
for _ in range(4):
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()

    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(100)
    turtle.end_fill()

    turtle.penup()
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)


turtle.done()
