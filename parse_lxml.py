import lxml.etree as ET
#from StringIO import StringIO
"""
To save the price of item in to dictionary
"""
d = {}
l_price =[]
l_name =[]

def parsebook(xmlfile):

#To create to list of price and menu   

    doc = ET.iterparse(xmlfile, events=('start','end'))
    for event,elem in doc:
        if event == 'end' and elem.tag =='name':
            l_name.append(elem.text)
        if event == 'end' and elem.tag == 'price':
            l_price.append(elem.text)

# Make a dictionary of menu and price
    count = 0
    for item in l_name:
        d[item] = l_price[count]
        count = count+1
            
    print d    

xmlfile = "C:\\Users\\pmahunta\\Desktop\\new\\food.xml"
parsebook(xmlfile)
    

    
