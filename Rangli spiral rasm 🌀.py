import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

t.speed(0)
t.width(2)

for i in range(200):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.left(59)

turtle.done()