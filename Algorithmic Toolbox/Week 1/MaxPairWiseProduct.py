def maxPairwiseProduct(numbers):
    p1 = max(numbers)
    numbers.remove(p1)
    p2 = max(numbers)
    return p1*p2

n = int(input())
numbers = list(map(int, input().split()))
print(maxPairwiseProduct(numbers))