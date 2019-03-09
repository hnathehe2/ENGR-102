# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  CFU 1
# Date:       September 13, 2018

import math
r=3.21 #radius
c_area=r*r*math.pi #calculate the area
c_peri=r*2*math.pi #calculate the perimeter
s_side1=math.sqrt(c_area) #find the first square side
s_side2=c_peri/4 #find the second square side
print("Area of the circle ",round(c_area,4)," and Perimeter of the circle",round(c_peri,4))
print("The side of the square that has same area ",round(s_side1,4))
print("The side of the square that has same perimeter ",round(s_side2,4))

