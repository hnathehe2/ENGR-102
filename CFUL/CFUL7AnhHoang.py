# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Anh Hoang
# Section:    506
# Assignment:  CFUL7
# Date:      October 11, 2018

n=int(input("Enter the number "))
while n>=0:
    i=1
    s=1
    print(n,"! is ",end='')
    while i<n:
        s=s*i
        print(i,"* ",end='')
        i=i+1
    if n!=0:
        s=s*n
        print(n,"= ",end='')
    print(s)
    n = int(input("Enter the number "))
print("Invalid Input")