import turtle

turtle.colormode(255)
turtle.shape("turtle")
turtle.speed("fastest")

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.left(90)


def get_colour(i):
    selections = [
        [1, 0, 0],
        [1, 0.5, 0],
        [1, 1, 0],
        [0.5, 1, 0],
        [0, 1, 0],
        [0, 1, 0.5],
        [0, 1, 1],
        [0, 0.5, 1],
        [0, 0, 1],
        [0.5, 0, 1],
        [1, 0, 1],
    ]
    return (
        int(selections[i % len(selections)][0] * 255),
        int(selections[i % len(selections)][1] * 255),
        int(selections[i % len(selections)][2] * 255),
    )


for i in range(10):
    colour = get_colour(i)
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(200 - i * 20, steps=6)
    turtle.penup()
    turtle.end_fill()

    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)

turtle.hideturtle()
turtle.done()
