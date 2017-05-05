import xml.etree.ElementTree as ET
import bisect

doc = ET.iterparse("C:\\Users\\pmahunta\\Desktop\\new\\xml\\sample.xml",event=('start','end'))
my_file = []
for event, elem in doc:
    if elem.tag == "Sup_ID" and event == 'end':
        bisect.insort(my_file,elem.text)
for item in my_file:
    print item
    
    
