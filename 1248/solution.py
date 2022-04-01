def find_parents(v):
    ps = []
    p = 0
    while p!=1:
        p = parent[v]
        ps.append(p)
        v = p
    return ps
def treesize(r):
    s = 0

    return s
TC = int(input())
for tc in range(1, TC+1):
    V, E, v1, v2 = map(int, input().split())
    parent = [0]*(V+1)
    edges = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        p, c = edges[i], edges[i+1]
        parent[c] = p
    print(parent)
    p1 = find_parents(v1)
    p2 = find_parents(v2)
    maxiter = min(len(p1), len(p2))
    commonroot = 1
    for i in range(-2, -maxiter, -1):
        print(p1[i], p2[i])
        if p1[i]!=p2[i]:
            commonroot = p1[i+1]
            break
    # find nearest common parent
    print(commonroot)
    ans = treesize(commonroot)