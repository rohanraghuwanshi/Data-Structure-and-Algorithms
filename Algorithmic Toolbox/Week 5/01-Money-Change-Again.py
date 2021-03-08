def money_change(m):
    denominations = [1, 3, 4]
    dp_result = [0] + [-1]*m
    for i in range(1, m+1):
        for j in denominations:
            if i >= j:
                coins = dp_result[i-j]+1
                if (coins < dp_result[i]) or (dp_result[i] == -1):
                    dp_result[i] = coins
    return dp_result[m]


m = int(input())
print(money_change(m))
