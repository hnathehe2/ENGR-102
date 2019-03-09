import numpy
x=[0]
y=[0]
s=[0]
d=[0]
n=int(input('Enter the amount of fixed points: '))
for i in range(1,n+1):
    print("The",i,"point")
    x.append(float(input("Enter the x ")))
    y.append(float(input("Enter the y ")))
    s.append(0)
    d.append(0)
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if x[i]>x[j]:
            q=x[i]
            x[i]=x[j]
            x[j]=q
            q=y[i]
            y[i]=y[j]
            y[j]=q
for i in range (1,n):
    s[i]=(y[i+1]-y[i])/(x[i+1]-x[i])
    d[i]=-x[i]*s[i]+y[i]
xin=float(input("Enter desire x "))
if xin<=x[1]:
    print(s[1]*xin+d[1])
elif xin>=x[n]:
    print(s[n-1]*xin+d[n-1])
else:
    for i in range(1,n):
        if (xin>x[i]) and (xin<=x[i+1]):
            print(s[i]*xin+d[i])
            break;