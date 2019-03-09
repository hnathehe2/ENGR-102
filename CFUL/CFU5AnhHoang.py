# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  CFU5
# Date:      September 27, 2018

HW=float(input("Your homework score "))
EX=float(input("Your exam score "))
PJ=(input("You did the project (True/False) "))
S=0.4*HW+0.6*EX
if PJ=="True":
    S=S+5
if (PJ=="True") and (S>=90):
    G="A"
elif S>=80:
    G="B"
elif S>=70:
    G="C"
elif S>=60:
    G="D"
else: G="F"
print("You total grade is",round(S,2)," Your letter grade is ",G)