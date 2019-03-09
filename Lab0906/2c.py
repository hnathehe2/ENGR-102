# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Anh Nghia Hoang
# Section:		506
# Assignment:	Lab 2b - activity 4 program 2b
# Date:		    06 09 2018
import numpy
import math
p1=numpy.array([1,3,7])
p2=numpy.array([23,-5,10])
t1=13
t2=84
dt=84-13
start=20
end=50
btw=(50-20)/4
init=20-13
speed=numpy.array((p2-p1)/dt)
for i in range (0,5):
    t3=init+i*btw
    p3=numpy.array(speed*t3+p1)
    print(p3)
    print("----------------");