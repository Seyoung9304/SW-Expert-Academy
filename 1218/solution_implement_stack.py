"""
Implemented Stack
Memory Used: 58,524 KB
Execution Time: 151 ms
"""
class Stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack)==0:
            return -1
        return self.stack.pop()
    
    def push(self, s):
        self.stack.append(s)
        

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
    Q = Stack()
    valid = 1
    for s in string:
        if s in lefts:
            Q.push(s)
        else:
            if pair[Q.pop()] != s:
                valid = 0
                break
    print(f"#{tc} {valid}")