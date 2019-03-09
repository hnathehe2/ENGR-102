# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab05_Assignment2
# Date:       September 25,2018

sex = input('What is your gender (Male or Female)? ') #Ask if they are a male or a female.
age = float(input('What is your age? '))                #Ask their age.
TC = float(input('What is your total Cholesterol? '))   #Ask for their total cholesterol
Smoke = input('Are you a smoker (True or False)? ')     #Ask if they are a smoker or not.
HDL = float(input('What is your High-Density Lipoprotein content (mg/DL) ')) #Ask what their HDL is.
SBPT = input('Have you had treatments for blood pressure (True/False)? ') #Ask if they have been treated for their blood pressure.
SBP= float(input('What is your Systolic BP (in mmHG) '))          #Ask what their systolic blood pressure is (in mmHg)
p = 0

if sex == 'Male':
#Compute points based on age and sex.
#Compute points based on total cholesterol,sex, and age.
#Compute points based on their smoking status,sex, and age.
#Compute points based on HDL, sex, and age.
    if (age<35) and (age>=20):
        p=p-9
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+4
        elif TC<240:
            p=p+7
        elif TC<280:
            p=p+9
        else: p=p+11
        if Smoke=='True':
            p=p+8
    elif age<40:
        p=p-4
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+4
        elif TC<240:
            p=p+7
        elif TC<280:
            p=p+9
        else: p=p+11
        if Smoke=='True':
            p=p+8
    elif age<45:
        p=p-0
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+3
        elif TC<240:
            p=p+5
        elif TC<280:
            p=p+6
        else: p=p+8
        if Smoke=='True':
            p=p+5
    elif age<50:
        p=p+3
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+3
        elif TC<240:
            p=p+5
        elif TC<280:
            p=p+6
        else: p=p+8
        if Smoke=='True':
            p=p+5
    elif age<55:
        p=p+6
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+2
        elif TC<240:
            p=p+3
        elif TC<280:
            p=p+4
        else: p=p+5
        if Smoke=='True':
            p=p+3
    elif age<60:
        p=p+8
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+2
        elif TC<240:
            p=p+3
        elif TC<280:
            p=p+4
        else: p=p+5
        if Smoke=='True':
            p=p+3
    elif age<65:
        p=p+10
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+1
        elif TC<240:
            p=p+1
        elif TC<280:
            p=p+2
        else: p=p+3
        if Smoke=='True':
            p=p+1
    elif age<70:
        p=p+11
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+1
        elif TC<240:
            p=p+1
        elif TC<280:
            p=p+2
        else: p=p+3
        if Smoke=='True':
            p=p+1
    elif age<75:
        p=p+12
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+0
        elif TC<240:
            p=p+0
        elif TC<280:
            p=p+1
        else: p=p+1
        if Smoke=='True':
            p=p+1
    else:
        p=p+13
        if TC<160:
            p=p+0
        elif TC<200:
            p=p+0
        elif TC<240:
            p=p+0
        elif TC<280:
            p=p+1
        else: p=p+1
        if Smoke=='True':
            p=p+1
    if HDL<40:
        p=p+2
    elif HDL<50:
        p=p+1
    elif HDL<60:
        p=p
    else: p=p-1
    if SBPT=='True':
        if SBP<130:
            p=p
        if SBP<160:
            p=p+1
        else:p=p+2
    else:
        if SBP<120:
            p=p
        if SBP<130:
            p=p+1
        if SBP<160:
            p=p+2
        else: p=p+3
    if p<5:
        o=1
    elif p<7:
        o=2
    elif p==7:
        o=3
    elif p == 8:
        o=4
    elif p==9:
        o=5
    elif p==10:
        o=6
    elif p==11:
        o=8
    elif p==12:
        o=10
    elif p==13:
        o=12
    elif p==14:
        o=16
    elif p==15:
        o=20
    elif p==16:
        o=25
    else: o=30
else:
    if 20 <= age < 35:
        p += -7
    elif 35 <= age < 40:
        p += -3
    elif 40 <= age < 45:
        p += 0
    elif 45 <= age < 50:
        p += 3
    elif 50 <= age < 55:
        p += 6
    elif 55 <= age < 60:
        p += 8
    elif 60 <= age < 65:
        p += 10
    elif 65 <= age < 70:
        p += 12
    elif 70 <= age < 75:
        p += 14
    else:
        p += 16
    if 20 <= age < 40:
        if TC < 160:
            p += 0
        elif 160 <= TC < 200:
            p += 4
        elif 200 <= TC < 240:
            p += 8
        elif 240 <= TC < 280:
            p += 11
        else:
            p += 13
    elif 40 <= age < 50:
        if TC < 160:
            p += 0
        elif 160 <= TC < 200:
            p += 3
        elif 200 <= TC < 240:
            p += 6
        elif 240 <= TC < 280:
            p += 8
        else:
            p += 10
    elif 50 <= age < 60:
        if TC < 160:
            p += 0
        elif 160 <= TC < 200:
            p += 2
        elif 200 <= TC < 240:
            p += 4
        elif 240 <= TC < 280:
            p += 5
        else:
            p += 7
    elif 60 <= age < 70:
        if TC < 160:
            p += 0
        elif 160 <= TC < 200:
            p += 3
        elif 200 <= TC < 240:
            p += 6
        elif 240 <= TC < 280:
            p += 8
        else:
            p += 10
    else:
        if TC < 160:
            p += 0
        elif 160 <= TC < 200:
            p += 1
        elif 200 <= TC < 240:
            p += 1
        elif 240 <= TC < 280:
            p += 2
        else:
            p += 2
    if Smoke == 'True':
        if 20 <= age < 40:
            p += 9
        elif 40 <= age < 50:
            p += 7
        elif 50 <= age < 60:
            p += 4
        elif 60 <= age < 70:
            p += 2
        else:
            p += 1
    else:
        p += 0

    if HDL < 40:
        p += 2
    elif 40 <= HDL < 50:
        p += 1
    elif 50 <= HDL < 60:
        p += 0
    else:
        p += -1
    if SBPT == 'True':
        if SBP < 120:
            p += 0
        elif 120 <= SBP < 130:
            p += 3
        elif 130 <= SBP < 140:
            p += 4
        elif 140 <= SBP < 160:
            p += 5
        else:
            p += 6
    else:
        if SBP < 120:
            p += 0
        elif 120 <= SBP < 130:
            p += 1
        elif 130 <= SBP < 140:
            p += 2
        elif 140 <= SBP < 160:
            p += 3
        else:
            p += 4
    if p<13:
        o=1
    elif 13<=p<15:
        o=2
    elif p==15:
        o=3
    elif p == 16:
        o=4
    elif p==17:
        o=5
    elif p==18:
        o=6
    elif p==19:
        o=8
    elif p==20:
        o=11
    elif p==21:
        o=14
    elif p==22:
        o=17
    elif p==23:
        o=22
    elif p==24:
        o=27
    else: o=30
print("Your total amount of points is",str(p),", and your 10 year risk is ",o,'%')