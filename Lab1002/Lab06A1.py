# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab06_Assignment1
# Date:       October 02 ,2018
# Test value A=5 B=2 C=3 D=4 a=-1 b=0  => root -0.83287406
# Test value A=1 B=1 C=1 D=1 a=-9 b=10  => root -1
# Test value A=1 B=3 C=-1 D=-1 a=0 b=10  => root 0.67513108
# Test value A=2 B=2 C=-1 D=-17 a=1 b=10  => root 1.82526508
# 1.	(x) is a continuous function in interval [a, b]
# 2.	f(a) * f(b) < 0
import math
A=float(input("What is the A coefficient: "))
B=float(input("What is the B coefficient: "))
C=float(input("What is the C coefficient: "))
D=float(input("What is the D coefficient: "))
a=float(input("What is the a bound: "))
b=float(input("What is the b bound: "))
c=(a+b)/2
fc=A*c*c*c+B*c*c+C*c+D
fa=A*a*a*a+B*a*a+C*a+D
fb=A*b*b*b+B*b*b+C*b+D
z=abs(fc)
count=0
if fa*fb<0:
    if (abs(fa)>0.000001) and (abs(fb)>0.000001):
        while z>0.000001:
            if fa*fc<0:
                b=c
                c=(a+b)/2
                fb=fc
                fc=A*c**3+B*c**2+C*c+D
                z=abs(fc)
            else:
                a=c
                c=(a+b)/2
                fa=fc
                fc = A * c**3+ B * c **2 + C * c + D
                z=abs(fc)
            count+=1
        print("The root is ",c)
        print("The iteration was done",count,"times")
    elif abs(fa)<= 0.000001:
        print("root is ",a)
        print("The iteration was done 1 time")
    else:
        print("root is ",b)
        print("The iteration was done 1 time")
else: print("The value you inout is out of bound ahihi")