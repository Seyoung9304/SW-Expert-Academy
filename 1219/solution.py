from collections import deque

TC = 10

for tc in range(TC):
    tc, n = map(int, input().split())
    pairs = list(map(int, input().split()))
    # in route: 0 if not connected, 1 if connected
    route = [[0]*100 for _ in range(100)]
    for i in range(0, n*2, 2):
        x, y = pairs[i], pairs[i+1]
        route[x][y] = 1
    visited = [False]*100
    Q = deque()
    Q.append(0)
    visited[0] = True
    endflag = False
    while Q:
        rt = Q.popleft()
        if rt==99:
            endflag = True
            break
        for i in range(100):
            if route[rt][i]==1 and visited[i]==False:   # if connected and not visited yet
                visited[i] = True
                Q.append(i)
    if endflag == True:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")