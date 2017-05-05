f= open("C:\\Users\\pmahunta\\Desktop\\new\\myfile.txt","r")
wc = 0
for i in f:
    
    f1 = i.split()
    wc = wc+len(f1)
    
f.close()
print wc

    
    
    
