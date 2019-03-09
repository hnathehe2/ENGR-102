# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  Lab 3b program 1
# Date:       September 13, 2018
import math
print("If you want to calculate a) The volume of a sphere Enter 1")
print("If you want to calculate b) The volume of a pyramid with a square base Enter 2")
print("If you want to calculate c) The kinetic energy of an object Enter 3")
print("If you want to calculate d) The rate constant of a chemical reaction Enter 4")
n=int(input("Enter the choice "))
if n==1:
    radius=float(input("Enter radius "))
    print("Volume of the sphere is ",(4/3)*math.pi*radius*radius*radius);
elif n==2:
    side=float(input("Enter side "))
    height=float(input("Enter height "))
    print("Volume of the pyramid is ",(1/3)*side*side*height);
elif n==3:
    mass=float(input("Enter mass "))
    velo=float(input("Enter velocity "))
    print("Kinetic energy is ",mass*velo*velo/2);
elif n==4:
    a_fact=float(input("Enter pre-exponential factor "))
    ener=float(input("Enter activation energy "))
    temp=float(input("Enter the temperature (in Kelvin) "))
    print("Rate constant of the chemical reaction is ",a_fact*math.e**(-ener/(8.314*temp)));