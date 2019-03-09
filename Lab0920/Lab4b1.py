# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  Lab4b 1
# Date:       September 20, 2018

import numpy
x=[1,1,1,1]
for i in range (1,5):
    x[i]=int(input("Input the number "))
for i in range (1,4):
    for j in range (i+1,4):
        if x[i]<x[j]:
            p=x[i];
            x[i]=x[j]
            x[j]=p
print("the largest number is ",x[1])