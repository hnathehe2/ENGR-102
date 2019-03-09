# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Anh Hoang
# Section:    506
# Assignment:  Lab04_Assignment2
# Date:       September 18, 2018
print("enter \"true\" (without \"\", just true) so that variable is true, any other input will consider if is false")
g=input("a = ")
a=(g=="true")
g=input("b = ")
b=(g=="true")
g=input("c = ")
c=(g=="true")
print("1 ",a and  b and c)
print("2 ",a or b or c)
print("3 ",(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b))
print("4 ",(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (xx not a or (a and b and c) or (a and ((b and not c) or (not b)))))
print("5 ",not a==b)
i=0;
if a: i+=1
if b: i+=1
if c: i+=1
print("6 ",(i==1)or(i==3))
print("7 ",(not a and not b) or  (not a and b and not c) or (a and not b))
print("8 ",(a)or (not a and not b and c))