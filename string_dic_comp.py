dict = {}
s = "poonam"
dic = {'p':1,'o':2,'n':1,'a':1,'m':1}
count = 1

def compa():
    for i in s:
        if i not in dict:
            dict[i] = count
        else:
            dict[i] = count+1
            
    print dic,dict
    if dic==dict:
        print "True"
    else:
        print "False"

compa()


'''def comp_str():
    t1 = "appUpdate"
    t2 = "appdUpate"
    d1 = {}
    d2 = {}

    for e in t1:
       if e not in d1:
           d1[e] = 1
       else:
           d1[e] = d1[e]+1
    print d1

    for e in t2:
       if e not in d2:
           d2[e] = 1
       else:
           d2[e] = d2[e]+1
    print d2

    if d1 == d2:
       print "True"
    else:
       print "False"

s = comp_str()'''       
