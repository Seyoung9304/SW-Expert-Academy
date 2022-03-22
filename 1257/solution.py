TC = int(input())
for tc in range(1, TC+1):
    substr = []
    K = int(input())
    string = input()
    l = len(string)
    for i in range(l):
        for j in range(i, l):
            substr.append(string[i:j+1])
    substr = set(substr)
    substr = list(substr)
    substr.sort()
    
    if len(substr) <= K:
        ans = "none"
    else:
        ans = substr[K-1]
    print(f"#{tc} {ans}")