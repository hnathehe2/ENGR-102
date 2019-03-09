# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab9
# Date:       October 30,2018

st=str(input("Enter the file name (remember end of file ex:.txt) "))
finput=open(st,'r+')
a=[]
n=int(finput.readline())
x=[0]
y=[0]
s=[0]
d=[0]
for i in range (1,n+1):
    st=str(finput.readline())
    a=st.split(",")
    x.append(int(a[0]))
    y.append(int(a[1]))
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
xin=(input("Enter desire point (enter stop to stop) "))
fout=open("answer.txt",'w')
while (xin !="stop"):
    xin=float(xin)
    fout.write("The value for {} is ".format(xin))
    if xin<=x[1]:
        fout.write(str(s[1]*xin+d[1]))
        fout.write('\n')
    elif xin>=x[n]:
        fout.write(str(s[n-1]*xin+d[n-1]))
        fout.write('\n')
    else:
        for i in range(1,n):
            if (xin>x[i]) and (xin<=x[i+1]):
                fout.write(str(s[i]*xin+d[i]))
                fout.write('\n')
                break;
    xin = (input("Enter desire point (enter stop to stop) "))
finput.close()
fout.close()
print("your answer is stored in answer.txt")