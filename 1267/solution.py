from collections import deque
# Topology sort
TC = 10
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    edges = list(map(int, list(input().split())))
    indegree = [0] * (V+1)
    child_parent = [[] for _ in range(V+1)]
    for i in range(0, 2*E, 2):
        parent = edges[i]
        child = edges[i+1]
        indegree[child] += 1
        child_parent[child].append(parent)

    # find start node
    todo = deque()   # work queue
    for i in range(1, V+1):
        if len(child_parent[i])==0:
            todo.append(i)
    
    print(f"#{tc}", end=" ")
    # topology sort
    while todo:
        p = todo.popleft()
        print(p, end=" ") # done
        for c in range(1, V+1):
            if p in child_parent[c]:
                indegree[c] -= 1
                if indegree[c]==0:
                    todo.append(c)
    print("")