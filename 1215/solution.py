def check_palin(s, p_len):
    for i in range(p_len//2):
        if s[i] != s[-1*(1+i)]:
            return 0
    return 1
    
T = 10
BOARD_SIZE = 8
for i in range(T):
    answer = 0
    arr = []
    p_len = int(input())
    for j in range(BOARD_SIZE):
        tmp = list(input())
        arr.append(tmp)
    # 가로
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE-p_len+1):
            substr = ""
            for j in range(p_len):
                substr += arr[row][col+j]
            answer += check_palin(substr, p_len)
    # 세로
    for row in range(BOARD_SIZE-p_len+1):
        for col in range(BOARD_SIZE):
            substr = ""
            for j in range(p_len):
                substr += arr[row+j][col]
            answer += check_palin(substr, p_len)
    print(f"#{i} {answer}")