def pisanoperiod(a):
    index=0
    for i in range(1,len(a)):
        if((a[i]==0) & (a[i+1]==1)):
            break
    index = i
    return index

def get_fibonacci(m): 
    x = m*m+1
    a = list()
    a0=0
    a1=1
    a.append(a0)
    a.append(a1)
    for _ in range(x):
        a0,a1 = a1,(a0+a1)%m
        a.append(a1)
    return(a)

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    a = pisanoperiod(get_fibonacci(m))
    previous = 0
    current  = 1
    g = n%a
    if g <= 1:
        return g

    for i in range(g-1):
        previous, current = current, previous + current
        if i % 10 == 0:
            previous, current =  previous , current
    return (current) %m


n = int(input())
k = get_fibonacci_huge_naive(n+2, 10)
if(k==0):
    print(9)
else:
    print(k-1)