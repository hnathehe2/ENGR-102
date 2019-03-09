def F(x):
    return (pow(x,3)+2*pow(x,2)+3*x-4)

def dev(x):
    return ((F(x + 0.0001) - F(x)) / 0.0001)

def new(x):
    return (x - F(x) / dev(x))

def Newtonstep(x):
    print(x - F(x) / dev(x))

a = float(input("Enter x: "))
i = a
kt = 1
print("List of successive approximations to a root")
while kt == 1:
    Newtonstep(i)
    if abs(i - new(i)) <= pow(10, -6):
        kt = 0
    i = new(i)