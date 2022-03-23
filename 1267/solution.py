TC = 10
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    edges = list(map(int, list(input().split())))
    indegree = [0] * (V+1)
    child_parent = [[] for _ in range(V+1)]
    for i in range(0, 2*E, 2):
        parent, child = edges[i], edges[i+1]
        indegree[child] += 1
        child_parent[child].append(parent)

    # find start node
    todo = []   # work queue
    for i in range(1, V+1):
        if len(child_parent[i])==0:
            todo.append(i)
    
    # topology sort
    front = 0
    while len(todo)<V:
        p = todo[front]
        for c in range(1, V+1):
            if p in child_parent[c]:
                indegree[c] -= 1
                if indegree[c]==0:
                    todo.append(c)
        front += 1

    print(f"#{tc}", end=" ")
    for i in todo:
        print(i, end=" ")
    print("")