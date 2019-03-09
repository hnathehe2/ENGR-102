import numpy as np
import matplotlib.pyplot as plt
numc = [0]
numd = [0]
domain1 = int(input("What is the 1st x domain: "))
domain2 = int(input("What is the 2nd x domain: "))

n = int(input("What is the largest degree in the polynomial? "))
for i in range(1,n+2):
    coef = int(input("What is the coefficient"))
    deg = int(input("What is the degree"))
    numc.append(coef)
    numd.append(deg)
x_val = [0]+np.arange(domain1,domain2,(domain2-domain1)/1000)
y = []
S=0
for j in range (1,len(x_val)-1):
    x=(x_val[j]+x_val[j+1])/2
    A=0
    for i in range(1,len(numc)):
        A = A + numc[i]*x**numd[i]
    S=S+A*(domain2-domain1)/1000
print("The answer is ",S)