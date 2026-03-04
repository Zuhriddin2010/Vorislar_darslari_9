#bu kodda rangbarang ranglar aylanadi
# import turtle as t
# import colorsys
# t.bgcolor('black')
# h = 1
# t.tracer(200)
# t.pensize(1)
# def drawing(a, n):
#     t.circle(5 + n, 60)
#     t.right(a)
#     t.circle(5 + n,60)
# t.goto(0, 0)
# for i in range(600):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h += 0.005
#     t.pencolor(c)
#     drawing(1/2, 0)
#     drawing(180, i)
# t.done()

#Bu koda ekranga sayyora rasmi chiziladi
# import turtle

# a = 0
# b = 0

# turtle.speed(18)
# turtle.bgcolor('black')
# turtle.pencolor('cyan')
# turtle.penup()
# turtle.goto(0, 200)
# turtle.pendown()

# while True:
#     turtle.forward(a)
#     turtle.right(b)
#     a += 3
#     b += 1