def inorder_traverse(root):
    if left[root]!=0:
        inorder_traverse(left[root])
    print(word[root], end="")
    if right[root]!=0:
        inorder_traverse(right[root])
    return

TC = 10
for tc in range(1, TC+1):
    Nnode = int(input())
    word = [0]*(Nnode+1)
    left = [0]*(Nnode+1)
    right = [0]*(Nnode+1)
    for _ in range(Nnode):
        tmp = input().split()
        try:
            idx = int(tmp[0])
            word[idx] = tmp[1]
            left[idx] = int(tmp[2])
            right[idx] = int(tmp[3])
        except:
            pass
    print(f"#{tc}", end=" ")
    inorder_traverse(1)
    print("")