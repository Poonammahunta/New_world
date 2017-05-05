import lxml.etree as ET
doc = ET.iterparse("C:\\Users\\pmahunta\\Desktop\\new\\xml\\sample.xml",events=('start','end'))

for event ,elem in doc:
    if event == "end" and elem.tag != "Suppliers":
        if doc.iterfind("Sup_ID") == "000041855":
            print "true"
        #print elem.getnext()
    else:
        print "false"
