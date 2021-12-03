# import sys
#
# INF = int(1e9)
#
#
# # sys.stdin = open('test1.txt', 'r')
# def get_array(): return list(map(int, sys.stdin.readline().split()))
#
#
# def get_ints(): return map(int, sys.stdin.readline().split())
#
#
# def input(): return sys.stdin.readline()
#
#
# import heapq
#
#
# def dijsktra(Adj, s, Ariel):
#     n = len(Adj)
#     dis = [INF] * (n + 1)
#     dis[s] = 0
#     stack = [(dis[s], s)]
#     while stack:
#         (g, v) = heapq.heappop(stack)
#         if v == Ariel:
#             break
#         if dis[v] != g: continue
#         for (w,u) in Adj[v]:
#             if dis[u] > dis[v] +w:
#                 dis[u] = dis[v] + w
#                 heapq.heappush(stack,(dis[u],u))
#     print(dis[Ariel] if dis[Ariel] !=INF else -1)
#
# def solver():
#     n_planet, n_space, s, t = get_ints()
#     Adj = [[] for x in range(n_planet+1)]
#     for i in range(n_space):
#         u, v, g = get_ints()
#         Adj[u].append((g, v))
#     dijsktra(Adj, s, t)
#
#
# if __name__ == '__main__':
#     solver()

# Python implementation of the approach
from typing import List
from queue import PriorityQueue
from sys import maxsize as INT_MAX

INF = 0x3f3f3f3f


# This class represents
# a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V: int) -> None:

        # Number of vertices
        self.V = V

        # In a weighted graph, store vertex
        # and weight pair for every edge
        self.adj = [[] for _ in range(V)]

    # Function to add an edge to the graph
    def addEdge(self, u: int, v: int, w: int) -> None:
        self.adj[v].append((u, w))

    # Function to find the shortest paths
    # from source to all other vertices
    def shortestPath(self, src: int, dist: List[int]) -> None:

        # Create a priority queue to
        # store vertices that
        # are being preprocessed
        pq = PriorityQueue()

        # Insert source itself in priority
        # queue and initialize
        # its distance as 0
        pq.put((0, src))
        dist[src] = 0

        # Loop till priority queue
        # becomes empty (or all
        # distances are not finalized)
        while not pq.empty():

            # The first vertex in pair
            # is the minimum distance
            # vertex, extract it from
            # priority queue
            u = pq.get()[1]

            # 'i' is used to get all
            # adjacent vertices of a vertex
            for i in self.adj[u]:

                # Get vertex label and
                # weight of current
                # adjacent of u
                v = i[0]
                weight = i[1]

                # If there is shorted
                # path to v through u
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    pq.put((dist[v], v))


# Function to return the
# required minimum path
def minPath(V: int, src: int, des: int, g: Graph, r: Graph) -> int:
    # Create a vector for
    # distances and
    # initialize all distances
    # as infinite (INF)

    # To store distance of all
    # vertex from source
    dist = [INF for _ in range(V)]

    # To store distance of all
    # vertex from destination
    dist2 = [INF for _ in range(V)]

    # To store distance of source
    # from all vertex
    dist3 = [INF for _ in range(V)]

    # To store distance of
    # destination from all vertex
    dist4 = [INF for _ in range(V)]

    # Computing shortest path from
    # source vertex to all vertices
    g.shortestPath(src, dist)

    # Computing shortest path from
    # destination vertex to all vertices
    g.shortestPath(des, dist2)

    # Computing shortest path from
    # all the vertices to source
    r.shortestPath(src, dist3)

    # Computing shortest path from
    # all the vertices to destination
    r.shortestPath(des, dist4)

    # Finding the intermediate node (IN)
    # such that the distance of path
    # src -> IN -> des -> IN -> src is minimum

    # To store the shortest distance
    ans = INT_MAX
    for i in range(V):

        # Intermediate node should not be
        # the source and destination
        if (i != des and i != src):
            ans = min(ans, dist[i] + dist2[i] + dist3[i] + dist4[i])

    # Return the minimum path required
    return ans


# Driver code
if __name__ == "__main__":
    # Create the graph
    V = 5
    src = 0
    des = 1

    # To store the original graph
    g = Graph(V)

    # To store the reverse graph
    # and compute distance from all
    # vertex to a particular vertex
    r = Graph(V)

    # Adding edges
    g.addEdge(0, 2, 1)
    g.addEdge(0, 4, 5)
    g.addEdge(1, 4, 1)
    g.addEdge(2, 0, 10)
    g.addEdge(2, 3, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 0, 5)
    g.addEdge(4, 2, 100)
    g.addEdge(4, 3, 5)

    # Adding edges in reverse direction
    r.addEdge(2, 0, 1)
    r.addEdge(4, 0, 5)
    r.addEdge(4, 1, 1)
    r.addEdge(0, 2, 10)
    r.addEdge(3, 2, 5)
    r.addEdge(1, 3, 1)
    r.addEdge(0, 4, 5)
    r.addEdge(2, 4, 100)
    r.addEdge(3, 4, 5)

    print(minPath(V, src, des, g, r))

# This code is contributed by sanjeev2552
