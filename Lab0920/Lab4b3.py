# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  Lab4b 3
# Date:       September 20, 2018

fvelo=int(input("Input Fluid velocity "))
kvisc=int(input("Input Kinematic viscosity "))
cdime=int(input("Input Characteristic linear dimension "))
reynum=fvelo*cdime/kvisc
if reynum<2300:
    print("Laminar")
elif (reynum<=4000) and (reynum>=2300):
    print("Transition")
elif reynum>4000:
    print("Turbulent")

print("According to the suggestion of the teacher")