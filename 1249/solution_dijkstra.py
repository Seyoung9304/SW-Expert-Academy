import heapq
INF = int(1e9)
TC = int(input())
MOVE = [[-1, 0], [1, 0], [0, -1], [0, 1]] # up, down, left, right
for tc in range(1, TC+1):
    SIZE = int(input())
    # map graph
    graph = []
    for _ in range(SIZE):
        graph.append(list(map(int, list(input()))))
    # distance graph, init with INF
    distance = [[INF]*SIZE for _ in range(SIZE)]
    # visited graph, init with False
    visited = [[False]*SIZE for _ in range(SIZE)]

    # dijkstra
    q = []
    heapq.heappush(q, (0, (0, 0)))  # push tuple - (distance, start point tuple)
    distance[0][0] = 0
    while q:
        # pop shortest node
        dist, now = heapq.heappop(q)
        i, j = now[0], now[1]
        if distance[i][j] < dist:
            continue
        for di, dj in MOVE:
            ni, nj = di+i, dj+j
            if 0<=ni<SIZE and 0<=nj<SIZE:
                cost = graph[ni][nj]+dist
                if cost < distance[ni][nj]:
                    distance[ni][nj] = cost
                    heapq.heappush(q, (cost, (ni, nj)))

    ans = distance[SIZE-1][SIZE-1]
    print(f"#{tc} {ans}")