# MST - Prim
import math

def prim():
    global graph, V
    MST_cost = 0
    MST = set([0]) # start from node 0
    not_visited = set(i for i in range(1, V))
    for _ in range(V-1):
        min_dist, next_node = math.inf, -1
        for node in MST:
            for to_node in not_visited:
                if graph[node][to_node] < min_dist:
                    min_dist = graph[node][to_node]
                    next_node = to_node
        not_visited.remove(next_node)
        MST.add(next_node)
        MST_cost += min_dist
    
    return MST_cost

TC = int(input())
for tc in range(1, TC+1):
    V = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    graph = [[0]*V for _ in range(V)]
    for i in range(V-1):
        for j in range(i, V):
            dist = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
            graph[i][j] = dist
            graph[j][i] = dist

    ans = round(prim()*E)
    print(f"#{tc} {ans}")