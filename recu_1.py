l = [23,12,56,[76,45],[98,54]]

def sum_all2(l):
    if len(l) == 0:
        return 0
    else:
        return l[0]+sum_all(l[1:])

def sum_all(l):
    total =0
    for elem in l:
        if (type(elem) == type(1)):
            total += elem
            print total

         else:
            total = total+sum_all(elem)
    return total

print sum_all(l)

        
            
