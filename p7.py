
from typing import List
import heapq


class ShortestPath:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append((u, v, weight))
        self.graph[u].append((v, weight))

    def dijkstra(self, src: int) -> List[int]:
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source node")

        dist = [float('inf')] * self.vertices
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            distance, u = heapq.heappop(pq)

            if distance > dist[u]:
                continue

            for v, weight in self.graph[u]:
                if weight < 0:
                    raise ValueError(
                        "Dijkstra does not support negative edges"
                    )

                new_dist = dist[u] + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return dist

    def bellman_ford(self, src: int) -> List[int]:
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source node")

        dist = [float('inf')] * self.vertices
        dist[src] = 0

        for _ in range(self.vertices - 1):
            changed = False

            for u, v, weight in self.edges:
                if dist[u] != float('inf'):
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        changed = True

            if not changed:
                break

        for u, v, weight in self.edges:
            if (dist[u] != float('inf')
                    and dist[u] + weight < dist[v]):
                raise ValueError("Negative-weight cycle detected")

        return dist


# Main program
sp = ShortestPath(5)

sp.add_edge(0, 1, 4)
sp.add_edge(0, 2, 1)
sp.add_edge(2, 1, 2)
sp.add_edge(1, 3, 1)
sp.add_edge(2, 3, 5)
sp.add_edge(3, 4, 3)

source = 0

print("Dijkstra distances:", sp.dijkstra(source))
print("Bellman-Ford distances:", sp.bellman_ford(source))
