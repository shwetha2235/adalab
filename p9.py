
def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)

    if len(weights) != len(values):
        raise ValueError("Weights and values must have equal length.")

    if capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("Weights and capacity cannot be negative.")

    dp = [0] * (capacity + 1)

    for i in range(n):
        for c in range(capacity, weights[i] - 1, -1):
            dp[c] = max(dp[c], values[i] + dp[c - weights[i]])

    return dp[capacity]


# Example
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Maximum value:", knapsack_01(weights, values, capacity))