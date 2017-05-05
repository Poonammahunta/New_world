#To open the csv file for address
f= open("C:\\Users\\pmahunta\\Desktop\\s_test.txt")
d = {}

for line in f.readlines():
    l = line.split(',')
    d[l[0]] = l[1:]
print d
    
       
    
    
    
