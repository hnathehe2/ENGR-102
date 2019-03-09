import numpy as np
import matplotlib.pyplot as plt


def PART1and2():
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
    plt.figure()
    for i in range(1, 46):
        plt.hist(consumers[i - 1], 50)
        plt.title("{} from 1990 to 2016".format(countries[i - 1]))
        plt.xlabel("Consumption range (MTOE)")
        plt.ylabel("Frequency of consumption")
        plt.show()
def PART7():
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
    plt.figure()
    plt.hist(consumers[26], 50)
    plt.title("China from 1990 to 2016")
    plt.xlabel("Consumption range (MTOE)")
    plt.ylabel("Frequency of consumption")
    plt.show()

PART7()
PART1and2()




#https://matplotlib.org/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py