# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment: CFU3
# Date:       September 20, 2018
import numpy
import math
print("Your name");
name=input()
s1=int(input("Your first test score\n"))
s2=int(input("Your second test score\n"))
s3=int(input("Your second test score\n"))
avg=(s1+s2+s3)/3
d1=s1-avg
d2=s2-avg
d3=s3-avg
Tavg=math.sqrt((d1**2+d2**2+d3**2)/2)
print(name," have mean score of ",avg," and deviation of ",Tavg)