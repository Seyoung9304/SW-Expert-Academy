from math import pow
def findpoint(idx, x1, x2):
    for i in range(100):
        cal = 0
        mid = (x1+x2)/2.0

        for j in range(idx+1):
            cal += weight[j] / ((x[j] - mid) ** 2)
        
        for j in range(idx+1, N):
            cal -= weight[j] / ((x[j] - mid) ** 2)

        if (abs(cal) <= pow(10, -13)):
            break
        elif (cal>0):
            x1 = mid
        elif (cal<0):
            x2 = mid
    return mid

TC = int(input())
for i in range(1, TC+1):
    N = int(input())

    tmp = list(map(int, input().split()))
    
    x = tmp[:N]
    weight = tmp[N:]

    print(f"#{i}", end=" ")
    for j in range(N-1):
        ans = findpoint(j, x[j], x[j+1])
        print(f"{ans : .10f}", end=" ")
    print("")

    
