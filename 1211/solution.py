TC = 10
LADDER_SIZE = 100
moves = [[0, 1], [0, -1], [1, 0]] # right, left, down
for _ in range(1, TC+1):
    ladder = []
    ans = 0
    # input
    tc = int(input())
    for row in range(LADDER_SIZE):
        ladder.append(list(input().split()))
    # DFS
    min_len = LADDER_SIZE**2
    for i in range(LADDER_SIZE):
        if ladder[0][i]=="1":
            visited = [[False]*LADDER_SIZE for _ in range(LADDER_SIZE)]
            l = 0
            col = i
            row = 0
            stack = [(row, col)]
            visited[row][col] = True
            while stack:
                p = stack.pop()
                for dr, dc in moves:
                    nr, nc = p[0]+dr, p[1]+dc
                    if 0<=nr<LADDER_SIZE and 0<=nc<LADDER_SIZE and ladder[nr][nc]=="1" and visited[nr][nc]==False:
                        row, col = nr, nc
                        visited[nr][nc] = True
                        stack.append((nr, nc))
                        break
                l += 1
            if min_len >= l:
                min_len = l
                ans = i
    # print
    print(f"#{tc} {ans}")