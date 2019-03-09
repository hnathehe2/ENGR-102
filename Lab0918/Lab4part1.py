# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#        Hanh Nguyen
#        Anh Hoang
#        Nicholas Arredondo
# Section:    506
# Assignment:  Lab04_Assignment1
# Date:       September 18, 2018

import math
import numpy
i=1;
a=i*5
b=10**math.log10(math.sqrt(i*5**2))
print("Is ",a," the same as ",b,"?",a==b,"\n")

i=1;
a=math.cos(i)
b=math.cos(math.acos(a))
print("Is ",a," the same as ",b,"?",a==b,"\n")

a = 1/19
b = 19*a
c = 2*a
d = 17*a
e = c+d
a = 1
print('Is',a,'equal to',e,":", a == e)


x = math.sqrt(3/4)
y = math.sqrt(1/4)
z = 2*(x**2+y**2)
a = 2
print('\nIs',a,'equal to',z,":", a == z)

x = math.sin(math.radians(45))
y = math.cos(math.radians(45))
z = x*y*2
a = 1
print('\nIs',a,'equal to',z,":", a == z)

x = numpy.log(45)
y = math.e
z = (y**x)
a = 45
print('\nIs',a,'equal to',z,":", a == z)

x=0.1
y=x+0.5
z=0.3+y
x=0.9
print('\nIs',x,'equal to',z,':', x==z)

a = math.pi/2
b = math.pi/2
c=(a+b)/math.pi
a=1
print('\nIs',a,'equal to',c,':', a==c)
print("\n $$$$$$$$$$$$$$$")
print("\n\n\nTolerance")
tol=0.00000000000001

i=1;
a=i*5
b=10**math.log10(math.sqrt(i*5**2))
print("Is ",a," the same as ",b,"?",a==b)
print("Is ",a," the same as ",b,"?",abs(a-b)<=tol,"\n")

i=1;
a=math.cos(i)
b=math.cos(math.acos(a))
print("Is ",a," the same as ",b,"?",a==b)
print("Is ",a," the same as ",b,"?",abs(a-b)<=tol,"\n")

a = 1/19
b = 19*a
c = 2*a
d = 17*a
e = c+d
a = 1
print('Is',a,'equal to',e,":", a == e)
print('Is',a,'equal to',e,":", abs(a-e)<=tol,"\n")


x = math.sqrt(3/4)
y = math.sqrt(1/4)
z = 2*(x**2+y**2)
a = 2
print('Is',a,'equal to',z,":", a == z)
print('Is',a,'equal to',z,":", abs(a-z)<=tol)

x = math.sin(math.radians(45))
y = math.cos(math.radians(45))
z = x*y*2
a = 1
print('\nIs',a,'equal to',z,":", a == z)
print('Is',a,'equal to',z,":", abs(a-z)<=tol)

x = numpy.log(45)
y = math.e
z = (y**x)
a = 45
print('\nIs',a,'equal to',z,":", a == z)
print('Is',a,'equal to',z,":", abs(a-z)<=tol)

x=0.1
y=x+0.5
z=0.3+y
x=0.9
print('\nIs',x,'equal to',z,':', x==z)
print('Is',x,'equal to',z,':', abs(x-z)<=tol)


a = math.pi/2
b = math.pi/2
c=(a+b)/math.pi
a=1
print('\nIs',a,'equal to',c,':', a==c)
print('Is',a,'equal to',c,':', abs(a-c)<=tol)

print("\n $$$$$$$$$$$$$$$")
print("\n\n\nTolerance size")
tol=0.00000000000000015
x = math.sin(math.radians(45))
y = math.cos(math.radians(45))
z = x*y*2
a = 1
g=(10**16+3)/(10**16)
h=(10**16+2)/(10**16)
print("a is ",a)
print("b is ",z)
print("x is ",g, " x=(10**16+3)/(10**16)")
print("y is ",h, " y=(10**16+2)/(10**16)")
print("tolerance is ",tol)
print('\nIs',a,'equal to',z,":", abs(a-z)<=tol)
print('Is',g,'equal to',h,":", abs(g-h)<=tol)