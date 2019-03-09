n=0
list=[]
list.append(0)
while n>=0:
        n=int(input("What is the number of widgets created today?: "))
        list.append(n)
list.pop(-1)
l=len(list)-1
ap = []
am = []
b = []
for i in range (0,l+1):
    am.append(0)
    ap.append(0)
    b.append(0)
for i in range(1,l):
    for j in range(1,l-i+1):
        if ((list[j]) < (list[j+i])):
            ap[i]=ap[i]+1
        elif ((list[j] > list[j+i])):
            am[i]=am[i]+1
        b[i]=b[i]+1
for i in range(1,l):
    print("For",i,"day interval",round(ap[i]/b[i]*100,1),"% were increasing and",round(am[i]/b[i]*100,1),"% were decreasing")