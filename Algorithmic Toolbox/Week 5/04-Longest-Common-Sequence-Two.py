import sys

def lcs2(a, b):
    m = len(a)
    n = len(b)

    L = [[None] * (n + 1) for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[i][j]


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

print(lcs2(a, b))