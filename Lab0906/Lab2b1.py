# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Anh Nghia Hoang
# Section:		506
# Assignment:	Lab 2b - activity 4 program 1
# Date:		    06 09 2018

import math
print('Anh Nghia Hoang UIN 228000790 ENGR 206 506')
print('Im an international student from Ho Chi Minh city, Vietnam, and this is the first time I come to America')
R=5;
I=20;
U=R*I
print('Ohm Law',U,'V')

mass=100;
v=21;
kine=mass*v*v/2;
print('Kinetic Energy',kine,'J')

v=100;
linear=2.5;
kine=1.2
reynum=v*linear/kine
print('Reynolds number',reynum)

tem=2200;
const=5.67*(10**(-8));
sblaw=tem**4*const;
print('Stephan Boltzmann Law',sblaw)

arps=(100**0.8/((0.8-1)*2))*(((100/(((1+(0.8*2*20))**(1/0.8))))**(1-0.8))-(100**(1-0.8)));
print('Arps equation',arps)

arate=20
srate=35
queue=arate*arate/(srate*(srate-arate))
print('M/M/1 Queue',queue)

cohe=2;
stress=20;
angle=35
Morh=cohe+stress*math.tan(angle/180*math.pi);
print('Mohr-Coulomb',Morh)

wave=7.5*(10**(-7))
dist=1*(10**(-6))
brag=math.asin((wave/(2*dist)))/math.pi*180
print('Brags Law',brag)