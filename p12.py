from typing import List

def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist


def optimal_bst(keys: List[int], freq: List[int]) -> int:
    n = len(keys)
    if n != len(freq):
        raise ValueError("Keys and frequencies must have equal length.")

    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float("inf")
            total = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0
                cost[i][j] = min(
                    cost[i][j], left + right + total
                )

    return cost[0][n - 1] if n else 0


# Example: Floyd-Warshall
INF = float("inf")
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

print("Shortest path matrix:")
for row in floyd_warshall(graph):
    print(row)

# Example: Optimal BST
keys = [10, 20, 30]
freq = [34, 8, 50]

print("Optimal BST cost:", optimal_bst(keys, freq))