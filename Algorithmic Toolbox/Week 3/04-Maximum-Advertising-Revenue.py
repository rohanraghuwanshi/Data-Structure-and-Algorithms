def maximum_advertising_revenue(a, b):
    a.sort()
    b.sort()

    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


data = list(map(int, input.split()))
n = data[0]
a = data[1:(n + 1)]
b = data[(n + 1):]
print(maximum_advertising_revenue(a, b))