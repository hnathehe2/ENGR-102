# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  Lab 3b program 3
# Date:       September 13, 2018

import numpy
import math

print("Enter the position of the observer");
x=float(input("x= "))
y=float(input("y= "))
z=float(input("z= "))
O=numpy.array([x,y,z])

print("Enter the first observed point");
x=float(input("x= "))
y=float(input("y= "))
z=float(input("z= "))
P1=numpy.array([x,y,z])

print("Enter the second observed point");
x=float(input("x= "))
y=float(input("y= "))
z=float(input("z= "))
P2=numpy.array([x,y,z])

V1=P1-O
V2=P2-O
V=numpy.dot(V1,V2)
mag1=math.sqrt(V1.dot(V1))
mag2=math.sqrt(V2.dot(V2))
degree=math.acos(V/(mag1*mag2))*180/math.pi

print("The angle between is ",round(degree,2))