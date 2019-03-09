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

n = int(input('Enter (n) as a positive integer: ')) # Asking user to input a positive integer
print(n,end=",") # Prints the first number in the sequence
count = 0 # starts counting amount of iterations taken to achieve expected output within the loop
# The while loop calculates the Collatz conjecture given a positive integer input from the user
while n > 1:
    if (n%2==0):
        # n is even
        n = n/2
    else:
        # n is odd
        n = 3*n +1
    if n!=1:
        print(round(n),end=",") # prints the rest of the numbers in the sequence
    else: print(round(n))
    count+=1
print('The amount of iterations to get to 1 using Collatz conjecture is',count)