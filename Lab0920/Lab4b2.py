# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  Lab4b 2
# Date:      September 20, 2018

import math
h=int(input("Input your height (in cm) "))
w=int(input("Input your weight (in kg) "))
BMI=w/((h/100)**2)
if BMI<18.5:
    print("You are underweight")
elif BMI<25:
    print("You are healthy")
elif BMI<30:
    print("You are overweight")
else:
    print("You are obese")
