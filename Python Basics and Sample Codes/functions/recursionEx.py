#fibonacci series

# 0 1 1 2 3 5 8 13 21 34 ...

'''fib(0)=0
    fib(1)=1
    fib(2) = fib(1)+fib(0)=1+0=1
    fib(3) = fib(2)+fib(1)=1+1=2
    fib(n)=fib(n-1)+fib(n-2) for n>1
'''
n = int(input("Enter the number of terms:"))

def fib(n):
    if (n==0 or n==1):   
        return n
    else:
        return fib(n-1)+fib(n-2)
    
print("Fibonacci series: " ,fib(n))
    