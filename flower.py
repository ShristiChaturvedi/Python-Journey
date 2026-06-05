import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(10)
pen.color("red")

# Draw flower petals
for i in range(36):
    pen.circle(100, 60)
    pen.left(120)
    pen.circle(100, 60)
    pen.left(170)

# Draw stem
pen.color("green")
pen.right(90)
pen.forward(200)

pen.hideturtle()

turtle.done()