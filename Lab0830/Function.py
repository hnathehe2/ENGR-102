# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Anh Nghia Hoang
# Section:      506
# Assignment:	Lab 1b - program 2
# Date:	        02 09 2018
import math;
print('This shows the evaluation of sin(x)/x evaluated close to x=0');
print('My guess is 0');
i=1;
print(math.sin(1));
print(math.sin(1)/1);
for x in range (1,7):
    i=i/10
    print(math.sin(i)/i);
print('This shows the evaluation of (1-cos(x))/(x^2) evaluated close to x=0');
print('My guess is 1')
i=1;
print((1-math.cos(i))/(i*i));
for x in range (1,7):
    i=i/10
    print((1 - math.cos(i)) / (i * i));
print('This shows the evaluation of (1+1/x)^x evaluated close to x=infinity');
print('My guess is +infinity')
i=1;
print((1+1/i)**i)
for x in range (1,7):
    i=i*10
    print((1+1/i)**i);
