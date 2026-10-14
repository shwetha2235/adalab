
from typing import List
from dataclasses import dataclass
import heapq


@dataclass
class Edge:
    u: int
    v: int
    weight: int


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges: List[Edge] = []

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append(Edge(u, v, weight))

    def kruskal_mst(self) -> List[Edge]:
        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        mst = []

        for edge in sorted(self.edges, key=lambda e: e.weight):
            if union(edge.u, edge.v):
                mst.append(edge)

            if len(mst) == self.vertices - 1:
                break

        if len(mst) != self.vertices - 1:
            raise ValueError("Graph is disconnected")

        return mst

    def prim_mst(self) -> List[Edge]:
        if self.vertices == 0:
            return []

        adj = [[] for _ in range(self.vertices)]

        for edge in self.edges:
            adj[edge.u].append((edge.weight, edge.v))
            adj[edge.v].append((edge.weight, edge.u))

        visited = set()
        heap = [(0, 0, -1)]
        mst = []

        while heap and len(visited) < self.vertices:
            weight, vertex, previous = heapq.heappop(heap)

            if vertex in visited:
                continue

            visited.add(vertex)

            if previous != -1:
                mst.append(Edge(previous, vertex, weight))

            for next_weight, neighbor in adj[vertex]:
                if neighbor not in visited:
                    heapq.heappush(
                        heap, (next_weight, neighbor, vertex)
                    )

        if len(visited) != self.vertices:
            raise ValueError("Graph is disconnected")

        return mst


# Main program
g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Kruskal MST:")
for e in g.kruskal_mst():
    print(e.u, "-", e.v, ":", e.weight)

print("\nPrim MST:")
for e in g.prim_mst():
    print(e.u, "-", e.v, ":", e.weight)
