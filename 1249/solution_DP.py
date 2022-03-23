TC = int(input())
for tc in range(1, TC+1):
    SIZE = int(input())
    graph = []
    for _ in range(SIZE):
        graph.append(list(map(int, list(input()))))
    for i in range(1, SIZE):
        graph[0][i] += graph[0][i-1]
        graph[i][0] += graph[i-1][0]
    for i in range(1, SIZE):
        for j in range(1, SIZE):
            graph[i][j] += min(graph[i-1][j], graph[i][j-1])

    ans = graph[SIZE-1][SIZE-1]
    print(f"#{tc} {ans}")