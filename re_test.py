l = ["ly","ior"]
import re
s = "Clearly, he has no excuse for such behavior"
for i in l:
    result = re.findall(i,s)
    result1 = re.search(i,s).start()
    print result,result1
    
