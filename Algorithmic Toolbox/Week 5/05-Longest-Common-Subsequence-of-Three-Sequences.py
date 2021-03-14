def lcs3(a,b,c):
    import numpy as np
    dp = np.zeros((len(a)+1, len(b)+1, len(c)+1)) 

    for i,num1 in enumerate(a):
        for j,num2 in enumerate(b):
            for k,num3 in enumerate(c):
                if num1 == num2 == num3:
                    dp[i+1][j+1][k+1] = dp[i][j][k]+1
                else:
                    dp[i+1][j+1][k+1] = max([dp[i+1][j+1][k],dp[i][j+1][k+1],dp[i+1][j][k+1]])
    return int(dp[len(a)][len(b)][len(c)])

na = int(input())
an = input()
a = an.split()
nb = int(input())
bn = input()
b = bn.split()
nc = int(input())
cn = input()
c = cn.split()
print(lcs3(a, b, c))