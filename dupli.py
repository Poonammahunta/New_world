import os
target = "C:\Users\pmahunta\Documents\Bill Details"

d = {}

for root,dirs,files in os.walk(target):
    for filename in [os.path.join(root,name)for name in files if name.endswith(".docx")]:
        
