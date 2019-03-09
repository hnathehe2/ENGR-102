# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:      Anh Hoang
# Section:    506
# Assignment:  Lab12_Assignment 12B
# Date:       November 26 2018
import turtle
import math
import random

number = int(input("Enter a number: "))  # Asking user to enter a number
t = turtle.Turtle()
t.right(90)
x = 0
dem=0
t.goto(0,0)
for i in range(1, number + 1):
    if (i%20 == 0):
        a=random.randint(120,150)
        t.right(a)
        b=random.randint(25,35)
        t.forward(b * math.sqrt(2))
        t.right(360-a)
        t.penup()
        t.goto(0, dem*40)
        t.pendown()
        x=0
        dem=dem+1
    elif (i % 5 == 0):
        a = random.randint(120, 150)
        t.right(a)
        t.forward(30 * math.sqrt(2))
        t.right(360-a)
    else:
        t.penup()
        t.goto(x * 10, dem*40)
        t.pendown()
        b=random.randint(25,35)
        a=random.randint(-10,10)
        t.right(a)
        t.forward(b)
        t.right(360-a)
    x = x + 1