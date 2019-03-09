import math
Vector_A = list()
## Asking for how many dimensions the vectors will have.
num = input("Enter how many Dimensions for vector A/B you want:")
#Creates the certain dimensioned vectors A.
print ('Enter Vector A')
for i in range(int(num)):
    n = input("num :")
    Vector_A.append(int(n))
Vector_B = list()
#Creates the certain dimensioned vectors B.
print ('Enter Vector B')
for i in range(int(num)):
    n = input("num :")
    Vector_B.append(int(n))

## Magnitude of Vector A
s=0
for row in range(0,len(Vector_A)):
    s=s+Vector_A[row]**2
s=math.sqrt(s)
print("\nMagnitude of Vector A is: ",s)
## Magnitude of Vector B
s=0
for row in range(0,len(Vector_B)):
    s=s+Vector_B[row]**2
s=math.sqrt(s)
print("Magnitude of Vector B is: ",s)
# Sum of Vector A and Vector B
Vector_C=list()
for i in range(0,len(Vector_A)):
    Vector_C.append(0)
for row in range(0,len(Vector_A)):
    Vector_C[row] = (Vector_A[row]+Vector_B[row])
print("Sum of vectors A and B is:",Vector_C)
# Difference of Vector A and B
for row in range(0,len(Vector_A)):
    Vector_C[row] = (Vector_A[row]-Vector_B[row])
print("Difference of Vector A and B is:",Vector_C)
s=0
# Dot Product of Vector A and B
for row in range(0,len(Vector_A)):
    s =s+ (Vector_A[row]*Vector_B[row])
print("Dot product of A B:",s)