import random


def partition(arr, left, right):
    pivot_value = arr[left]
    p_l = i = left
    p_e = right
    while i <= p_e:
        if arr[i] < pivot_value:
            arr[i], arr[p_l] = arr[p_l], arr[i]
            p_l += 1
            i += 1
        elif arr[i] == pivot_value:
            i += 1
        else:
            arr[i], arr[p_e] = arr[p_e], arr[i]
            p_e -= 1
        pIndexes = [p_l, p_e]
    return pIndexes


def randomized_quick_sort(arr, left, right):
    if left >= right:
        return

    pivot = random.randint(left, right)
    arr[left], arr[pivot] = arr[pivot], arr[left]
    pIndex = partition(arr, left, right)
    randomized_quick_sort(arr, left, pIndex[0] - 1)
    randomized_quick_sort(arr, pIndex[1] + 1, right)


n = int(input())
arr = list(map(int, input().split()))
randomized_quick_sort(arr, 0, n - 1)
for x in arr:
    print(x, end=' ')