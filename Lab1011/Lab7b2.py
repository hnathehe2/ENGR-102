# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab7b_Prog2
# Date:       11 Oct 2018
# username and passwords are case sensitive
a={} # dictionary used to store username values
b={} # dictionary used to store password values
n=int(input("Input the number of accounts ")) # How many username and password pairs will be entered by the user
print("Enter the user names") # Allows user to input the amount of user names to be stored
for i in range(1,n+1):
    s=str(input())
    a[s]=i
print("Enter the passwords") # Allows user to input the amount of passwords to be stored
for i in range(1,n+1):
    s=str(input())
    b[s]=i
ac=0
pw=0
test=0
for i in range(1,10):
    print()
while test==0:
        s=str(input("User name: ")) # Gathers a username from the user
        t=str(input("User password: ")) # Gathers a password  from the user
        if s in a:          # if username and password combination is correct, the user gains access
            ss=a[s]         # if the username and password combination is incorrect, the user is prompted to retry until correct
            if t in b:
                tt=b[t]
                if ss==tt:
                    test=1
                    print("Congratulations, you have gained the access!")
                else:
                    print("Wrong password baby, try again")
            else: print("Wrong password baby, try again")
        else:
            print("Wrong username baby, try again")
        print()
print("Wish you a good day <3")