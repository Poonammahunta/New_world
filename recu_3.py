def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1)+fib(n-2))

inp = int(raw_input("Enter number of terms: "))

for i in range(inp):
    print fib(i)



def fib(n):
    if n == 0:
        return 0
    else:
        return (n%10)+fib(n/10)
    
print fib(572)

def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-2)

print sum(10)    
