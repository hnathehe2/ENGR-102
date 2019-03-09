import numpy as np
import matplotlib.pyplot as plt

inp=open('EnergyConsumers.txt','r')
d=0
year=[]
consumers=[]
countries=[]
for line in inp:
    d=d+1
    line=line.strip('\n')
    line=line.split('\t')
    if (d==3):
        j=0
        for i in line:
            j=j+1
            if j>1:
                year.append(int(i))
    if (d>3):
        j=0
        for i in line:
            j=j+1
            if j>1:
                consumers.append(float(i))
            else:
                countries.append(i)
consumers=np.reshape(consumers,(d-3,len(year)))
consumers15=[]
for j in range (0,d-3):
    consumers15.append(consumers[j,25])
print(consumers15)