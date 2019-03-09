# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab06B_Assignment3
# Date:       October 04,2018

import math
d=1;
print("Enter the",d,"number ") #input 1st number
x=int(input())
if x>=0:
    min=x
    max=x   #creat min max
else:
    min=max=0
avg=0
while x>=0:   #use while loop
    avg=(avg*(d-1)+x)/d  #new mean
    d=d+1
    if min>x: min=x    #check new min
    if max<x: max=x    #check new max
    print("Enter the", d, "number ")
    x=int(input())     #input new number
print("The average is",avg)
print("The minimum number is",min)
print("The maximum number is",max)