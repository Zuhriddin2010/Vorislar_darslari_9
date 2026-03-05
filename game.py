# Bu o`yinda hatolik bor

# from turtle import *
# import colorsys
# bgcolor("black")
# tracer(500)


# def draw():
#     h = 0
#     for i in range(75):
#         c = colorsys.hsv_to_rgb(h, 1, 1)  # Get color based on hue
#         h += 0.01  # Smaller hue increment for smooth color transition

#         up()
#         goto(0, 0)  # Move turtle to the center
#         down()

#         color('black')
#         fillcolor(c)  # Set the fill color

#         begin_fill()
#         rt(98)  # Turn right 98 degrees
#         circle(i, 12)  # Draw part of a circle with radius 'i' and extent 12

#         fd(290)  # Fixed movement forward (290 units)
#         fd(i)  # Dynamic forward movement based on 'i'

#         lt(29)  # Turn left 29 degrees

#         for j in range(10):  # Reduced inner loop iterations for better control
#             fd(2 * i)  # Forward movement based on 'i'
#             circle(j, 50, steps=2)  # Draw smaller polygons inside the shape

#         end_fill()  # End the fill after the shape is drawn


# draw()
# done()


# import turtle as t

# t.bgcolor("#eeeeee")
# t.speed(8)
# t.width(4)
# t.penup()
# t.lt(90)
# t.fd(100)
# t.lt(87)
# t.pendown()
# t.color('black')
# t.begin_fill()
# t.circle(180,30)
# t.rt(70)
# t.fd(30)
# t.circle(5,150)
# t.fd(40)
# t.circle(-60,30)
# t.fd(10)
# t.circle(60,30)
# t.rt(10)
# t.fd(40)
# t.circle(190,40)
# t.circle(70,90)
# t.circle(190,40)
# t.fd(40)
# t.rt(10)
# t.circle(60,30)
# t.fd(10)
# t.circle(-60,30)
# t.fd(40)
# t.circle(5,150)
# t.fd(30)
# t.rt(70)
# t.circle(180,30)
# t.end_fill()
# t.color('sky blue')
# t.rt(5)
# t.circle(180,25)
# t.circle(15,75)
# t.fd(40)
# t.circle(15,55)
# t.fd(60)
# t.rt(70)
# t.fd(10)
# t.rt(45)
# t.fd(10)
# t.rt(85)
# t.circle(80,50)
# t.lt(45)
# t.fd(10)
# t.lt (80)
# t.fd(30)
# t.circle(40,50)
# t.fd(10)
# t.rt(60)
# t.fd(30)
# t.lt(100)
# t.circle(-37,80)
# t.lt(100)
# t.fd(30)
# t.rt(60)
# t.fd(10)
# t.circle(40,50)
# t.fd(30)
# t.lt(80)
# t.fd(10)
# t.lt (45)
# t.circle(80,50)
# t.rt(85)
# t.fd(10)
# t.rt(45)
# t.fd(10)
# t.rt(70)
# t.fd(60)
# t.circle(15,55)
# t.fd(40)
# t.circle(15,75)
# t.circle(180,30)
# t.penup()
# t.goto(-106,-50)
# t.pendown()
# t.lt(105)
# t.circle(90,40)
# t.rt(30)
# t.fd(40)
# t.rt(60)
# t.circle(90,20)
# t.penup()
# t.goto(106,-50)
# t.pendown()
# t.rt(12)
# t.circle(-90,40)
# t.lt(30)
# t.fd(40)
# t.lt (60)
# t.circle(-90,20)
# t.penup()
# t.goto(-30,-35)
# t.width(1)
# t.rt(65)
# t.pendown()
# t.begin_fill()
# t.circle(-37,90)
# t.rt(115)
# t.fd(25)
# t.circle(-15,38)
# t.fd(20)
# t.end_fill()
# t.penup()
# t.goto(30,-35)
# t.pendown()
# t.begin_fill()
# t.circle(37,90)
# t.lt(115)
# t.fd(25)
# t.circle(15,38)
# t.fd(20)
# t.end_fill()
# t.hideturtle()
# t.done()

#quiz
# def check_guess(guess, answer):
#     global score
#     still_guessing = True
#     attempt = 0
#     while still_guessing and attempt < 3:
#         if guess.lower() == answer.lower():
#             print("To'g'ri javob")
#             score = score + 1
#             still_guessing = False
#         else:
#             if attempt < 2:
#                 guess = input("Kechirasiz, noto'g'ri javob, qayta urinib ko'ring  >>")
#             attempt = attempt + 1
#     if attempt == 3:
#         print("To'g'ri javob ",answer )
    
# score = 0
# print("Hayvonni taxmin qil")
# guess1 = input("Shimoliy Qutbda qaysi ayiqlar yashaydi? ")
# check_guess(guess1, "qutb ayiqi")
# guess2 = input("Eng tez yuruvchi hayvon qaysi? ")
# check_guess(guess2, "Chita")
# guess3 = input("Eng katta hayvon qaysi?  ")
# check_guess(guess3, "Ko`k Kit")
# print("Your Score is "+ str(score))

