"""
재귀 ver 순열로 풀면 된다고 ,,
"""
def bigger(a, b):
    a = int(a)
    b = int(b)
    return str(max(a, b))

T = int(input())
for tc in range(1, T+1):
    N, C = input().split()
    C = int(C)
    len_N = len(N)
    if C*2 >= len_N:
        N = list(str(N))
        N.sort(reverse=True)
        if (C*2-len_N)%2==1:
            tmp = N[-2]
            N[-2] = N[-1]
            N[-1] = tmp
        ans = ''.join(N)
        print(f"#{tc} {ans}")
    else:
        # swap
        ans = N
        while C:
            for i in range(len_N):
                for j in range(len_N):
                    change = ans
                    change = list(change)
                    tmp = change[i]
                    change[i] = change[j]
                    change[j] = tmp
                    change = ''.join(change)
                    ans = bigger(change, ans)
            C-=1
        print(f"#{tc} {ans}")