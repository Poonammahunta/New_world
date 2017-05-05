import codecs

f = codecs.open("C:\\Users\\pmahunta\\Desktop\\new\\cat\\test.docx",encoding='utf-8',errors='ignore',mode='r')
s = f.readlines()
for i in s:
    print i.encode('utf-8')
f.close()    

    
