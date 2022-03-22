"""
그리디 말고 중복조합으로 다시 풀기
"""
T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    ans = 1

    basenum = N // P
    left = N % P
    
    for _ in range(P - left):
        ans *= basenum
    
    basenum += 1
    for _ in range(left):
        ans *= basenum

    print(f"#{tc} {ans}")