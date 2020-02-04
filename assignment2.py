# Author: Ben Nichols
# Date: January 20th, 2019
# This program prompts a user to choose an option to draw something using turtle

# Import turtle graphics

import turtle

# Prompt user to choose an option

print("Enter 1 to draw a line.")
print("Enter 2 to draw a circle.")
print("Enter 3 to draw a square.")
print("Enter 4 to draw an equilateral triangle")
userInt = float(input("\nEnter here: "))

# Prompt user to input unit of measurement or terminate program if invalid input

if (userInt == 1):
    
    length = float(input("\nInput the length of the line: "))
    direction = input("Enter the direction of the line (N,E,S,W): ")

    # Set direction 

    if (direction == "N"):
        turtle.setheading(90)
    elif (direction == "E"):
        turtle.setheading(0)
    elif (direction == "S"):
        turtle.setheading(270)
    elif (direction == "W"):
        turtle.setheading(180)
    else:
        print("Invalid direction, program terminating")

    # Move turtle amount determined by user

    turtle.forward(length)

elif (userInt == 2):

    radius = float(input("\nInput the radius of the circle: "))

    # Create circle with x radius determined by user

    if radius < 0:

        radius = (radius * -1)

    turtle.penup()
    turtle.setpos(0, -radius)
    turtle.pendown()
    
    turtle.circle(radius)

elif (userInt == 3):

    length = float(input("\nInput the length of the square: "))

    # Move turtle to bottom left of square so square is in the middle of screen

    if length < 0:

        length = (length * -1)

    turtle.penup()
    turtle.setpos(-(length/2),-(length/2))
    turtle.pendown()

    # Draw square with x length determined by user
    
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)

elif (userInt == 4):

    length = float(input("\nInput the length of the triangle: "))

    turtle.forward(length/2)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length/2)

else:

    print("\nInvalid input! No option selected. Program terminating")
    
print("\nEnd")
