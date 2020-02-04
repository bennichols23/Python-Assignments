# Assignment 4
# Ben Nichols
# February 6th, 2019

import turtle
turtle.hideturtle()

def cSquare (xc, yc, l):
    turtle.penup()
    turtle.goto(xc, yc)
    turtle.pendown()
    for a in range (4):
        turtle.forward(l)
        turtle.left(90)

def main():
    x = int(input("Enter the X coordinate: "))
    y = int(input("Enter the Y coordinate: "))
    l = int(input("Enter the length of the square: "))
    cSquare(x, y, l)

main()
