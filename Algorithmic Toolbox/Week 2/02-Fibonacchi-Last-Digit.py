def calcLastDigit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        previous, current = current, (previous + current)	
        if (i%10 == 0):
        	previous, current = previous%10,current%10

    return current % 10

n = int(input())
print(calcLastDigit(n))