CODELEN = 56

CODE_DICT = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}

def verify_code(code):
    # 연산 중복 제거
    odds = code[0]+code[2]+code[4]+code[6]
    evens = code[1]+code[3]+code[5]+code[7]
    if (odds*3 + evens) % 10 == 0:
        return odds+evens
    else:
        return 0

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    done = False
    for j in range(N):
        code = list(input())
        if "1" in code and not done:
            # find code index range
            start, end = 0, 0
            # find last index of code
            # every code's last digit is "1"
            for idx in range(M-1, 0, -1):
                if code[idx] == "1":
                    end = idx
                    break
            start = end - CODELEN + 1
            # extract real code 
            realcode = []
            # decode into decimal code
            for idx in range(start, end, 7):
                tmp = "".join(code[idx:idx+7])
                realcode.append(CODE_DICT[tmp])
            # verify code
            answer = verify_code(realcode)
            done = True
            print(f"#{i+1} {answer}")