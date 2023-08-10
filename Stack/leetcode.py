class Solution():
    def isValid(self, s: str) -> bool:    
        if len(s) % 2 == 1: 
            return False
        stack = []
        dictionary = {'(':')', '{':'}','[':']'}
        for x in s:
            if x in dictionary:
                stack.append(x)
            elif len(stack) == 0 or dictionary[stack.pop()] != x:
                return False
        return len(stack) == 0 
            
# leetcode 155
class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            val = min(self.min[-1],val)
        self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min[-1]


                