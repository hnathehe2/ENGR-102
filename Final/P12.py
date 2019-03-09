import numpy as np

def PART12():
    inp=open('EnergyConsumers.txt','r')
    d=0
    year=[]
    consumers=[]
    countries=[]
    total=[]
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
            s=0
            for i in line:
                j=j+1
                if j>1:
                    consumers.append(float(i))
                    s=s+float(i)
                else:
                    countries.append(i)
            total.append(s)
    consumers=np.reshape(consumers,(d-3,len(year)))
    trace=[]
    for i in range (0,len(countries)):
        trace.append(i)
    for i in range(0,len(countries)-1):
        for j in range(i,len(countries)):
            if total[j]>total[i]:
                s=total[j]
                total[j]=total[i]
                total[i]=s
                s=trace[i]
                trace[i]=trace[j]
                trace[j]=s
    print("Countries with highest energy consumption from 1990 to 2016")
    print("The top 4 is\t",total[0],'\t',total[1],'\t',total[2],'\t',total[3])
    print("Countries   \t",countries[trace[0]],'\t\t\t',countries[trace[1]],'\t\t\t',countries[trace[2]],'\t\t\t\t',countries[trace[3]])
    print("Continents  \t North America\t\t\t Asia\t\t\t Europe\t\t\t\t\t Asia")

PART12()
