line = [4,6,7]
t = int(raw_input("Enter the value: "))
def foo():
    for i in line:
        if i > t:
            t = i
        print i
        
