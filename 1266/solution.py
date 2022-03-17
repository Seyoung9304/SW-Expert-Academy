from math import pow
not_prime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
C = [[1]*19 for _ in range(19)]
for i in range(1, 19):
    for j in range(1, i):
        C[i][j] = C[i-1][j-1] + C[i-1][j]

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    a /= 100
    b /= 100
    a_fail = 1.0 - a
    b_fail = 1.0 - b
    p_a = 0
    p_b = 0
    for n in not_prime:
        combi = C[18][n]
        p_a += (pow(a, n)) * (pow(a_fail, 18-n)) * combi
        p_b += (pow(b, n)) * (pow(b_fail, 18-n)) * combi
    ans = 1.0000000 - p_a*p_b
    print("#{0} {1:.6f}".format(tc, ans))