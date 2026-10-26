from typing import List

class GraphBacktracker:
    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.n = len(graph)

    def graph_coloring(self, m: int) -> List[int]:
        colors = [0] * self.n

        def solve(v):
            if v == self.n:
                return True

            for c in range(1, m + 1):
                if all(
                    not self.graph[v][u] or colors[u] != c
                    for u in range(self.n)
                ):
                    colors[v] = c
                    if solve(v + 1):
                        return True
                    colors[v] = 0

            return False

        return colors if solve(0) else []

    def hamiltonian_cycle(self) -> List[int]:
        path = [0] + [-1] * (self.n - 1)

        def solve(pos):
            if pos == self.n:
                return self.graph[path[-1]][path[0]] != 0

            for v in range(1, self.n):
                if (v not in path[:pos] and
                    self.graph[path[pos - 1]][v] != 0):
                    path[pos] = v
                    if solve(pos + 1):
                        return True
                    path[pos] = -1

            return False

        if self.n == 0:
            return []

        return path + [path[0]] if solve(1) else []


# Example
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

g = GraphBacktracker(graph)

print("Vertex colors:", g.graph_coloring(3))
print("Hamiltonian cycle:", g.hamiltonian_cycle())