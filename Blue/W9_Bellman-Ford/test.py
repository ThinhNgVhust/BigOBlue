# INF = int(1e9)
# Adj = [(1, 1, -1), (1, 0, 1), (0, 0, 0), (0, 1, 1)]
# dis = [0, INF]
# V = 2
# # lan1
# for i in range(V - 1):
#     for edge in Adj:
#         u, v, w = edge[0], edge[1], edge[2]
#         if dis[u] != INF and dis[v] > dis[u] + w:
#             dis[v] = dis[u] + w
# # lan2
# for i in range(V - 1):
#     for edge in Adj:
#         u, v, w = edge[0], edge[1], edge[2]
#         if dis[u] != INF and dis[v] > dis[u] + w:
#             dis[v] = -INF
# print(dis)


INF = int(1e9)
Adj = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, -1)]
dis = [0, INF]
V = 2
# lan1
for i in range(V - 1):
    for edge in Adj:
        u, v, w = edge[0], edge[1], edge[2]
        if dis[u] != INF and dis[v] > dis[u] + w:
            dis[v] = dis[u] + w
# lan2
for i in range(V):
    for edge in Adj:
        u, v, w = edge[0], edge[1], edge[2]
        if dis[u] != INF and dis[v] > dis[u] + w:
            dis[v] = -INF
print(dis)
