#Name = ques5.py
import math
temp = 1
s = int(raw_input("Enter how many input: "))
while True:
    if s <= temp:
        D = int(raw_input("Enter digits: "))
        temp += temp
        print tuple(D)
        continue
        
        
C = 50
H = 30
Q = math.sqrt((2*C*D)/H)
print int(Q)



    

