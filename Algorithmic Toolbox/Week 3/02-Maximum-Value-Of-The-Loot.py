def get_optimal_value(capacity, weights, values):
    value = 0.
    proportion = [float(v) / float(w) for v, w in zip(values, weights)]
    for _ in range(len(weights) + 1):
        if capacity == 0:
            return value
        max_weight = max(proportion)
        index = proportion.index(max_weight)
        proportion[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        weights[index] -= add_capacity
        capacity -= add_capacity
    return value

n, capacity = list(map(int, input().split()))
values = []
weights = []
for i in range(n):
    a, b = list(map(int, input().split()))
    values.append(a)
    weights.append(b)
opt_value = get_optimal_value(capacity, weights, values)
print("{:.10f}".format(opt_value))