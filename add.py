l = int(raw_input("Enter the value: "))
new_l = str(l)
#new_l = len(str(l))
def add(l):
    temp = 0
    for i in range(len(new_l)):
        
        temp = temp+ int(new_l[i])
    print temp
    
        
add(l)


