foo = open("myfile.txt","r+")
pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
l = ""
d = {}
for i in foo.readlines():
    for j in pun:
        if j in i:
            i.replace(j,"")
        print i
    
      
            
            
            
