"""
Used Deque
Memory Used: 59,572 KB
Execution Time: 175 ms
"""     
from collections import deque
TC = 10
for tc in range(1, TC+1):
    tclen, string = input().split()
    stack = deque()
    for s in string:
        try: 
            if stack[-1]==s:
                stack.pop()
            else:
                stack.append(s)
        except:
            stack.append(s)
    password = ''.join(stack)
    print(f"#{tc} {password}")