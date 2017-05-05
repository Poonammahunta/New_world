def mod(s,temp,l):
    while True:
        if s >= temp:
            d = int(raw_input("Enter the values: "))
            temp = temp+1
            l.append(d)
            continue
        else:
            break
    return l    
    

if __name__ == "__main__":
    mod(2,1,1)
    print "sucess"
else:
    print "cll"


    
        


