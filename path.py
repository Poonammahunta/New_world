f1 = open("C:\\Users\\pmahunta\\Desktop\\new\\cat\\fa_test.txt","r")
f2=  open("C:\\Users\\pmahunta\\Desktop\\new\\cat\\fo_test.txt","w")

def sed(f1,f2):
    try:
        s = f1.readlines()
        for item in s:
            if item not in f2.readline():
                print item
                f2.write(item)
                

    except:
        print "Error encountered"
        f2.close()
    

                    
sed(f1,f2)


f1.close()
f2.close()
            
            
    
    
    
    
        
        
    
    
