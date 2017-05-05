import math
import module
s=int(raw_input("Enter how many digits for output: "))
temp = 1
l = []
D = module.mod(s,temp,l)
print D
C = 50
H = 30
Q = []
for i in D:
        q = math.sqrt((2*C*i)/2)
        Q.append(int(q))
print tuple(Q)
