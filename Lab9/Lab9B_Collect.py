# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab9_Challenge
# Date:       October 31,2018

a_file = str(input("what is the Data file name (with .txt format please)? "))
list_name = []
with open(a_file,"w") as file:
    num_dep = int(input("How many dependent variables will you have? "))
    for i in range(0,num_dep):
        dep = input("What is the dependent variable? ")
        list_name.append(dep)
    n = int(input('Enter the amount of fixed points: '))
    file.write(str(n))
    file.write('\n')
    for i in range(1, n + 1):
        print("The", i, "point")
        x = input("Enter the time: ")
        file.write(x)
        file.write('\n')
    file.write(str(num_dep))
    file.write('\n')
    for i in range(0,num_dep):
        for j in range(1, n+1):
            print("The", j, "point for dependent value ",list_name[i])
            x = input("Enter the {}: ".format(list_name[i]))
            file.write(x)
            file.write('\n')


