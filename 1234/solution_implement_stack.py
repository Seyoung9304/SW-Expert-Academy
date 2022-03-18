"""
Implemented Stack
Memory Used: 58,244 KB
Execution Time: 145 ms
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

    def seek(self):
        if len(self.stack)==0:
            return -1
        return self.stack[-1]

    def showstack(self):
        return ''.join(self.stack)
        
TC = 10
for tc in range(1, TC+1):
    tclen, string = input().split()
    stack = Stack()
    for s in string:
        if stack.seek()==s:
            stack.pop()
        else:
            stack.push(s)
    password = stack.showstack()
    print(f"#{tc} {password}")