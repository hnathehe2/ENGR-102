# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Final project
# Date:       December 7,2018

import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import defaultdict

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
    for i in range(1, 44):
        plt.hist(consumers[i - 1], 50)
        plt.title("{} from 1990 to 2016".format(countries[i - 1]))
        plt.xlabel("Consumption range (MTOE)")
        plt.ylabel("Frequency of consumption")
        plt.show()

def PART3and4():

    columns = defaultdict(list)
    with open('EnergyRawDataFinal.txt','r') as EnergyRaw:
        reader = csv.DictReader(EnergyRaw)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)
    Nation= []
    for i in range(0,2288):
        if columns['Nation'][i] == columns['Nation'][i-1]:
            continue
        else:
            Nation.append(columns['Nation'][i])
    Year= []
    for i in range(0,2288):
        if columns['Year'][i] == columns['Year'][i-1]:
            continue
        else:
            for j in range(0,44):
                Year.append(columns['Year'][i])


    Consumptions= [float(i) for i in columns['Consumptions']]

    Electricity = []
    Natural_Gas= []
    for i in range (0,2288):
        if i%2 != 0:
            Natural_Gas.append(Consumptions[i])
        else:
            Electricity.append(Consumptions[i])

    objects = ('Electricity (MTOE) ', 'Natural Gas (BCM)')
    y_pos = np.arange(len(objects))
    for i in range(0,1144):
        data = []
        data.append(Electricity[i])
        data.append(Natural_Gas[i])
        plt.bar(y_pos,data, align ='center', alpha = 0.5)
        plt.xticks(y_pos,objects)
        plt.ylabel('Consumption')
        plt.title("Comparison of Energy Consumption for {} for the year: {}".format(Nation[i],Year[i]))
        plt.show()

def PART5and6():
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
    Ind=[]
    IndB = []
    for i in range(0,1188):
        if i%27 ==0:
            for j in range(i,i+11):
                Ind.append(consumers[j] * (15 / 100))
            for k in range(i+11,i+27):
                IndB.append(consumers[k] * (35 / 100))

    consumers=np.reshape(consumers,(d-3,len(year)))
    inp.close()



    for i in range(0,len(countries)):
        Inblue =[]
        Inred =[]
        for j in range(i*11,i*11+11):
            Inblue.append(Ind[j])
        for k in range(i*16,i*16+16):
            Inred.append(IndB[k])
        num_bins = 10
        plt.hist([Inblue,Inred],num_bins, color = ['blue', 'red'])
        plt.legend(['Prior to 2001', 'From 2001 to 2016'])
        plt.xlabel('Industrial Energy Consumptions (MTOE)')
        plt.ylabel('Frequency of that Consumption')
        plt.title("Comparison of Energy for {} for the year 1990-2016".format(countries[i]))
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

def PART8and9():
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
    con = ('Europe',"Asia",'North America',"South America","Africa","Middle East")
    continents = defaultdict(list)

    for i in range(0, len(con)):
        for j in range(0,27):
            if i == 0:
                for q in range(0,14):
                    if 0<=j<11:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.85)
                    else:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.65)
            if i == 1:
                for q in range(14,18):
                    if 0<=j<11:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.85)
                    else:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.65)
                for q in range(26,36):
                    if 0<=j<11:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.85)
                    else:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.65)
            if i == 2:
                for q in range(18,20):
                    if 0<=j<11:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.85)
                    else:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.65)
            if i == 3:
                for q in range(20,26):
                    if 0<=j<11:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.85)
                    else:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.65)
            if i == 4:
                for q in range(36,40):
                    if 0<=j<11:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.85)
                    else:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.65)
            if i == 5:
                for q in range(40,44):
                    if 0<=j<11:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.85)
                    else:
                        continents['{}'.format(con[i])].append(consumers[j+(q*27)]*0.65)

    for i in range(0,len(continents)):
        Inblue =[]
        Inred =[]
        for j in range(i,154):
            Inblue.append(continents['{}'.format(con[i])])
        for k in range(154,379):
            Inred.append(continents['{}'.format(con[i])])
        num_bins = 10
        plt.hist([Inblue,Inred],num_bins, color = ['blue', 'red'])
        plt.legend(['Prior to 2001', 'From 2001 to 2017'])
        plt.xlabel('Residential Energy Consumptions (MTOE) for each Continent')
        plt.ylabel('Frequency of that Consumption')
        plt.title("Comparison of Energy for {} for the year 1990-2017".format(con[i]))
        plt.show()

def PART10():
    CEmis = open('CarbonEmissions.txt', 'r')
    allRows = []
    for s in CEmis:
        s = s.strip('\n')
        s = s.split('\t')
        allRows.append(s)
    return allRows

def PART11():
    #carbon emissions
    import csv
    import matplotlib.pyplot as plt

    CEmis = open('CarbonEmissions.txt', 'r')
    reader = csv.reader(CEmis)
    allRows=[]
    for s in CEmis:
        s = s.strip('\n')
        s = s.split('\t')
        allRows.append(s)

    #2015 values
    import numpy as np


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
    consumer_name =[]
    for j in range (0,d-3):
        if j==26 or j==19 or j==27 or j==15 or j==29 or j==3 or j==31 or j==40 or j==18 or j==42 or j==21 or j==24 or j==28 or j==39 or j==11 or j==34 or j==4 or j==13 or j==2 or j==6:
            consumers15.append(consumers[j,25])
            consumer_name.append(countries[j])
    compare =[]
    compare_name =[]

    for t in consumer_name:
        for p in range(1,21):
            for q in range(0,3):
                if q == 1:
                    if allRows[p][q] == t:
                        compare_name.append(t)
                        compare.append(float(allRows[p][2]))

    #comparison graph
    import matplotlib.pyplot as plt
    plt.figure(figsize=(25,5))
    ax=plt.subplot(111)
    ax.bar(compare_name, compare,width=0.4,color='b',align='center')
    ax2=ax.twinx()
    ax2.bar(compare_name, consumers15,width=0.2,color='r',align='center')
    plt.suptitle("Carbon Emission vs. Consumer Energy Consumption(2015)\nBlue is Carbon Emission; Red is Energy Consumption for 2015")
    plt.ylabel('Unit for energy consumption is MTOE')
    plt.show()

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
    print("Countries with highest energy consumption from 1990 to 2016 (Part 12)")
    print("The top 4 is\t",total[0],'\t',total[1],'\t',total[2],'\t',total[3])
    print("Countries   \t",countries[trace[0]],'\t\t\t',countries[trace[1]],'\t\t\t',countries[trace[2]],'\t\t\t\t',countries[trace[3]])
    print("Continents  \t North America\t\t\t Asia\t\t\t Europe\t\t\t\t\t Asia")

PART1and2()
PART3and4()
PART5and6()
PART7()
PART8and9()
print(PART10())
PART11()
PART12()