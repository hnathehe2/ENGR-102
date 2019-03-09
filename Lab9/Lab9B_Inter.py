# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:    Shion Ito
#           Hanh Nguyen
#           Anh Hoang
#           Nicholas Arredondo
# Section:    506
# Assignment:  Lab9_Challenge
# Date:       October 31,2018

w=(input("Enter desire point (enter stop to stop) "))
xin=[0]
fout=open("answer.txt",'w')
while (w !="stop"):
    xin.append(float(w))
    w =(input("Enter desire point (enter stop to stop) "))
st=str(input("Enter the file name (remember end of file ex:.txt) "))
finput=open(st,'r+')
n=int(finput.readline())
x=[0]

for i in range(1,n+1):
    st = str(finput.readline())
    x.append(int(st))

k=int(finput.readline())

for i in range (1,k+1):
    y=[0]
    s=[0]
    d=[0]
    for j in range(1, n + 1):
        st = str(finput.readline())
        y.append(int(st))
        s.append(0)
        d.append(0)
    for j in range(1,n):
            s[j] = (y[j + 1] - y[j]) / (x[j + 1] - x[j])
            d[j] = -x[j] * s[j] + y[j]
    fout.write("Dependent {} \n".format(i))
    for u in range(1,len(xin)):
        fout.write("For T{}: ".format(u))
        if xin[u]<=x[1]:
            fout.write(str(s[1]*xin[u]+d[1]))
            fout.write('\n')
        elif xin[u]>=x[n]:
            fout.write(str(s[n-1]*xin[u]+d[n-1]))
            fout.write('\n')
        else:
            for z in range(1,n):
                if (xin[u]>x[z]) and (xin[u]<=x[z+1]):
                    fout.write(str(s[z]*xin[u]+d[z]))
                    fout.write('\n')
                    break;
finput.close()
fout.close()
print("your answer is stored in answer.txt")