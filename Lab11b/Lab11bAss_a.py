import math
p=math.pi

def Cal1(w,l,h,r):
    print("The remaining is ",w*l*h-p*r*r*h)

def Cal2(w,l,h,r):
    i=math.asin(w/24/r)
    i=p/2-i
    i=i*2
    i=p*r*r*(i/2/p)
    j=math.sqrt(r*r-w*w/4)
    j=j*w/2
    print(2*h*(w*l/2-i-j))

def Cal3(w,l,h,r):
    a1=2*math.acos((l/2)/r)
    a2=2*math.acos((w/2)/r)
    a3=2*p-2*a1-2*a2 #goc cua 4 goc nho luon
    d1=math.sqrt(r*r-l*l/4)
    s1=d1*l/2 #dien tich cua tam giac ben A
    d2=math.sqrt(r*r-w*w/4)
    s2=d2*w/2 #dien tich cua tam giac ben B
    s=p*r*r #dien tich hinh tron
    print(w*l-2*s1-2*s2-a3*s/2/p)


a= float(input("Enter the width "))
b= float(input("Enter the length "))
height= float(input("Enter the height "))
radius= float(input("Enter the radius "))
if (a>b):
    c=a
    a=b
    b=c
if radius<=a/2:
    Cal1(a,b,height,radius)
elif (radius<=b/2): Cal2(a,b,height,radius)
elif (radius<=(math.sqrt(a*a+b*b))/2): Cal3(a,b,height,radius)
else: print(0)