"""
Using Deque
Memory Used: 62,880 KB
Execution Time: 192 ms
"""

from collections import deque

lefts = '([{<'
rights = ')]}>'

pair={
    '(': ')', 
    '[': ']', 
    '{': '}', 
    '<': '>'
}

TC = 10
for tc in range(1, TC+1):
    tclen = int(input())
    string = input()
    Q = deque()
    valid = 1
    for s in string:
        if s in lefts:
            Q.append(s)
        else:
            if pair[Q.pop()] != s:
                valid = 0
                break
    print(f"#{tc} {valid}")