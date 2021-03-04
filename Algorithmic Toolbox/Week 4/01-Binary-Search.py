def binary_search(arr, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))
n = data1[0]
arr = data1[1:]

for x in data2[1:]:
    high, low = len(data1[2:]), 0
    result = binary_search(arr, low, high, x)
    print(result, end=' ')