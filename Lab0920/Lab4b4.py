# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  Lab4b 4
# Date:      September 20, 2018

import math
d=int(input("Input the day "))
print("The total product is ")
if d<10:
    print(d*10)
elif d<60:
    print(10*10+(d-10)*40)
else:
    x=0
    for i in range(61,d+1):
        x=x+i-60
    print(10*10+50*40+40*(d-60)-x)