TC = 10
MAZE_SIZE = 100
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(1, TC+1):
    tc = int(input())
    maze = []
    visited = [[False]*MAZE_SIZE for _ in range(MAZE_SIZE)]
    start_idx = (0, 0)
    end_idx = (0, 0)
    ans = 0
    """
    # input
    find_2 = False
    find_3 = False
    for row in range(MAZE_SIZE):
        tmp = list(input()) 
        maze.append(tmp)
        if find_2==False and "2" in tmp:
            start_idx = (row, tmp.index("2"))
            find_2=True
        if find_3==False and "3" in tmp:
            end_idx = (row, tmp.index("3"))
            find_3=True  
    """
    # input ver 2 - Faster
    find_2 = False
    find_3 = False
    for row in range(MAZE_SIZE):
        maze.append(list(input()))
    for row in range(MAZE_SIZE):
        if find_2==False and "2" in maze[row]:
            start_idx = (row, maze[row].index("2"))
            find_2=True
        if find_3==False and "3" in maze[row]:
            end_idx = (row, maze[row].index("3"))
            find_3=True  

    # DFS
    stack = [start_idx]
    visited[start_idx[0]][start_idx[0]] = True
    while stack:
        p = stack.pop()
        if p==end_idx:
            ans = 1
            break
        for dx, dy in moves:
            nx, ny = p[0]+dx, p[1]+dy
            if 0<=nx<MAZE_SIZE and 0<=nx<MAZE_SIZE and maze[nx][ny]!="1" and visited[nx][ny]==False:
                stack.append((nx, ny))
                visited[nx][ny] = True
    # print
    print(f"#{tc} {ans}")