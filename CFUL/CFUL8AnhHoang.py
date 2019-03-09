# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  CFUL8
# Date:      October 18, 2018

import numpy
feet=[0]
inch=[0]
cm=[0]
print("Enter 1 height in feet and inches")
inf=float(input("Enter Feet "))
ini=float(input("Enter Inches "))
n=1
while (inf>0) or (ini>0):
    feet.append(inf)
    inch.append(ini)
    cm.append((inf*12+ini)*2.54)
    n=n+1;
    print("Enter",n,"height in feet and inches")
    inf = float(input("Enter Feet "))
    ini = float(input("Enter Inches "))
for i in range (1,n):
    print(i,"Input:",feet[i],"feet and",inch[i],"inches is",cm[i],"centimeters")
