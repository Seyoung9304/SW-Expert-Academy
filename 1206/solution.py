T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    b_len = int(input())
    b_list = list(map(int, input().split()))
    answer = 0
    for i in range(2, b_len-2):
        h = b_list[i]
        m1 = max(b_list[i-2:i])
        m2 = max(b_list[i+1:i+3])
        m = max(m1, m2)
        answer += max(0, h-m)
    print(f"#{test_case} {answer}")
