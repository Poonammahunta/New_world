#l = [1,2,3,4,6,8,5]
#F = 0
def max(l,F):
    for i in l:
        if i > F:
            F = i
        else:
            F = F
    print F

l = [1,2,8,5,9,4,10,0]
F = 0
max(l,F)
