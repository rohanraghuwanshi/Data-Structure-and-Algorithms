def maximum_advertising_revenue(a, b):
    a.sort()
    b.sort()

    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(maximum_advertising_revenue(a, b))