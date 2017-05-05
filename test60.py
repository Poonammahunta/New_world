foo = open("my.txt","r")
foo = foo.readlines()
d = {}

for i in foo:
    i = i.split()
    for j in i:
        d[j] = i.count(j)
print d    
