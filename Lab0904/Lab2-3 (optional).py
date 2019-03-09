# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Anh Nghia Hoang
# Section:		506
# Assignment:	Lab 2 - program 3 (optional challenge)
# Date:		    04 09 2018
import math
lap=2*0.5*1000*math.pi;
t1=30
t2=45
d1=50
d2=615
s=(d2-d1)/(t2-t1)
t20m=20*60-30
d20m=s*t20m+50
d20m=d20m%lap
print('the distant of the car after 20m is', d20m)