# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab9
# Date:       October 30,2018

a_file = str(input("what is the Data file name (with .txt format please)? "))

with open(a_file,"w") as file:
    ind = input("What is the independent variable? ")
    dep = input("What is the dependent variable? ")
    n = int(input('Enter the amount of fixed points: '))
    file.write(str(n))
    file.write('\n')
    for i in range(1, n + 1):
        print("The", i, "point")
        x = input("Enter the {}: ".format(ind))
        y = input("Enter the {}: ".format(dep))
        file.write(x+','+y)
        file.write('\n')