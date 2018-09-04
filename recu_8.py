def foo(n):
   if len(str(n)) == 1:
       return n
   else:
       return (n%10)+foo(n/10)

print foo(345)    
 
    
 
