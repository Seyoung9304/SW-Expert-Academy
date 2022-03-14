def checkp(s, p_len):
    for i in range(p_len//2):
        if s[i] != s[-1*(1+i)]:
            return 0
    return 1
    
T = 10
BOARD_SIZE = 8
for i in range(T):
    answer = 0
    p_len = int(input())
    arr = []
    cnt = 0
    for j in range(BOARD_SIZE):
        tmp = list(input())
        arr.append(tmp)
    # 가로
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE-p_len+1):
            str1 = ""
            for j in range(p_len):
                str1 += arr[row][col+j]
            answer += checkp(str1, p_len)
    # 세로
    for row in range(BOARD_SIZE-p_len+1):
        for col in range(BOARD_SIZE):
            str2 = ""
            for j in range(p_len):
                str2 += arr[row+j][col]
            answer += checkp(str2, p_len)
    print(f"#{i+1} {answer}")
