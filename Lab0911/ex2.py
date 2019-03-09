# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#        Hanh Nguyen
#        Anh Hoang
#           Matthew Witkowski
# Section:    506
# Assignment:  Lab03_Assignment2
# Date:       September 11, 2018

import numpy
n=['1','1','1','1']
b=['1','1','1','1']
for x in range (0,4):
       n[x]=(input("Name of the person "))
       b[x]=(input("Birthday of the person "))

for x in range (0,4):
       print(n[x].center(40),' ',b[x].rjust(40))
