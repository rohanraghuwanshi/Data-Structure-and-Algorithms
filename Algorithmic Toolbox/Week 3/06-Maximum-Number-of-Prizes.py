def optimal_summands(n):
    summands = []
    for i in range(1, n + 1):
        n -= i
        if n <= i:
            summands.append(n + i)
            break
        elif n == 0:
            summands.append(i)
            break
        else:
            summands.append(i)
    return summands


n = int(input())
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')