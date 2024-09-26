import math
import turtle

# Functions to define the heart shape
def heart_x(k):
    return 15 * math.sin(k)**3

def heart_y(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Set up the Turtle environment
turtle.speed(200011111)
turtle.bgcolor('black')
turtle.color('red')
turtle.pensize(1)

# Draw the heart shape
turtle.penup()
turtle.goto(heart_x(0) * 15, heart_y(0) * 15)
turtle.pendown()

for i in range(1000):
    k = i / 100
    turtle.goto(heart_x(k) * 15, heart_y(k) * 15)
    if i % 360 == 0:
        turtle.color('red')



turtle.hideturtle()
turtle.done()