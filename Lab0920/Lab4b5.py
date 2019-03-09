# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  Lab4b 5
# Date:      September 20, 2018

import math
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
if (a==b==c==0):
    print("There are infinite roots")
elif (a==b==0) and (c!=0):
    print("There is no root")
elif (a==0) and (b!=0):
    print("There is 1 root")
    print(-c/b)
else:
    delta=b**2-4*a*c
    if delta==0:
        print("There is 1 real root")
        print(-b/(2*a))
    elif delta>0:
        print("There are 2 real roots")
        print(-b/(2*a)+math.sqrt(delta)/(2*a))
        print(-b/(2*a)-math.sqrt(delta)/(2*a))
    elif delta<0:
        print("There are 2 unreal roots")
        print(-b/(2*a),"+",math.sqrt(-delta)/(2*a),'i')
        print(-b/(2*a),"-",math.sqrt(-delta)/(2*a),'i')