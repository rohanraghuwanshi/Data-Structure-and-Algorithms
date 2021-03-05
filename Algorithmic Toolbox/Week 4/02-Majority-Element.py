def get_majority_element(arr, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return arr[left]

    left_elem = get_majority_element(arr, left, (left + right - 1) // 2 + 1)
    right_elem = get_majority_element(arr, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if arr[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if arr[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1


n = int(input())
arr = input()
if get_majority_element(arr, 0, n) != -1:
    print(1)
else:
    print(0)