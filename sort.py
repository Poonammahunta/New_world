import xml.etree.ElementTree as ET
tree = ET.parse("sampleout.xml")
container = tree.find("Supliers")
data = []
for elem in container:
    ID = elem.findtext("Sup_ID")
    data.append((ID,elem))
data.sort()
container[:] = [items for items in data]
tree.write("new_data.xml")    
    
    
    


