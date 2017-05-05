import lxml.etree as ET

dom = ET.parse("sample.xml")
xslt = ET.parse("static.xsl")
transform = ET.XSLT(xslt)
newdom = transform(dom)
f = open("sorted_xsltout.xml","w")
f.write(str(newdom))
f.close()
