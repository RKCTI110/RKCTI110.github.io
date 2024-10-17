# CTI 110
# P2LAB2B - Turtles
# KeeferR
# 10/17

#using lists and loops to draw

import turtle
t = turtle.Turtle()
#remember, pensize, pencolor
t.pensize(6)
t.pencolor("blue")


# simple loop
for length in [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]:
    t.forward(length)
    t.right(90)

t.pencolor("green")
for length  in [75, 55, 35, 15, 35, 55, 75]:
    t.forward(length)
    t.right(45)

sides = 7
length = 100
angle = 360 / sides

for color in ["red", "black", "blue", "orange", "red", "green", "black"]:
    t.pencolor(color)
    t.forward(length)
    t.right(angle)
    

