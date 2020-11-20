def calcFibonacci(n):
    if (n <= 1):
        return n
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(n):
    	fib.append(fib[i]+fib[i+1])


    return fib[n] 

n = int(input())
print(calcFibonacci(n))