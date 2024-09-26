import math
import turtle

# Functions to define the heart shape
def heart(k):
    return 15 * math.sin(k) ** 3

def heart1(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Set up the Turtle environment
turtle.speed(1111111111)
turtle.bgcolor('black')
turtle.color('red')
turtle.pensize(1)

# Draw the heart shape
turtle.penup()
turtle.goto(0, 60)
turtle.pendown()

for i in range(1100):
    turtle.goto(heart(i) * 15, heart1(i) * 15)
    if i % 360 == 0:
        turtle.color('red')



# Hide the turtle
turtle.hideturtle()
turtle.done()