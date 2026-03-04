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

# import turtle as t
# import colorsys
# t.bgcolor("black")
# t.tracer(100)
# t.pensize(1)
# h=0.5
# for i in range(250):
#     c=colorsys.hsv_to_rgb(h,1,1 )
#     h=0.0008
#     t.fillcolor(c)
#     t.begin_fill()
#     t.fd(i)
#     t.lt(100)
#     t.circle(30)
#     for j in range(2):
#         t.fd(i*j)
#         t.rt(109)
#         t.end_fill()

# Bu kod aylana 360 aylanadi
# from turtle import *

# speed(0)
# bgcolor("black")
# colors = ["orange", "white"]
# hideturtle()
# for i in range(122):
#   goto(0,0)
#   color(colors[i%2])
#   forward(130)
#   left(3)
#   circle(40)
#   forward(130)
#   right(180)

# done()

# from turtle import *
# import colorsys 
# tracer(5)
# h=0.7
# bgcolor("black")
# pensize(2)

# for i in range(190): 
#       c=colorsys.hsv_to_rgb(h,1,1)
#       color(c)
#       h+0.004
#       circle(190-i,90)
#       lt(90)
#       lt(20)
#       circle(190-i,90)
#       lt(18)
# done()

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
for i in range(20):
  for j in range(20):
    box = Button(color=color.white, model='cube', position=(j,0,i),
          texture='grass.png', parent=scene, origin_y=0.5)
    boxes.append(box)

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)

app.run()