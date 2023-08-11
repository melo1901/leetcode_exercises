from typing import List
import math

class Solution():
    # leetcode 20
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
    
    # leetcode 150
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result, temp, flag = 0, 0, 0
        while tokens != []:
            if len(tokens) == 1 and stack == []:
                return int(tokens[0])
            try:
                if -200 <= int(tokens[0]) <= 200:
                    stack.append(int(tokens[0]))
                    tokens.remove(tokens[0])
                    flag += 1
            except ValueError:                
                if tokens[0] == "+":
                    if flag >= 2:
                        temp = stack.pop()
                        result = stack.pop() + temp
                    else:
                        result = stack.pop() + stack.pop()
                    tokens.remove(tokens[0])
                    stack.append(result)
                    flag -= 1
                elif tokens[0] == "-":
                    if flag >= 2:
                        temp = stack.pop()
                        result  = stack.pop() - temp
                    else:
                        result = stack.pop() - stack.pop()
                    tokens.remove(tokens[0])
                    stack.append(result)
                    flag -= 1
                elif tokens[0] == "/":
                    if flag >= 2:
                        temp = stack.pop()
                        result = int(stack.pop() / temp)
                    else:
                        result += int(stack.pop() / stack.pop())
                    tokens.remove(tokens[0])
                    stack.append(result)
                    flag -= 1
                elif tokens[0] == "*":
                    if flag >= 2:
                        temp = stack.pop()
                        result = stack.pop() * temp
                    else:
                        result = stack.pop() * stack.pop()
                    tokens.remove(tokens[0])
                    stack.append(result)
                    flag -= 1
        return result
            
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


                