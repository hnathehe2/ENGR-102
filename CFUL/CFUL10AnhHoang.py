# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  CFU10
# Date:      November 8, 2018


import math


def change(a, b):
    print("The x,y coordinate is (", a * math.cos(b), ",", a * math.sin(b), ")")


r = float(input("Enter r coordinate: "))
t = float(input("Enter theta coordinate: "))
change(r, t / 180 * math.pi)
