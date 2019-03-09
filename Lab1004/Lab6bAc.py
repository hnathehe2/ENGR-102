# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab06B_Assignment3
# Date:       October 04,2018

import math
#2 for loop to check every situation
for y in range(2, 101):
    for x in range(2, y+1):
        if y % x == 0:
            print(x, "divides", y)
