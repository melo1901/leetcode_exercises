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
        # first solution
        
        # stack = []
        # result, flag= 0, 0
        # for i in range(len(tokens)):
        #     if len(tokens) == 1 and stack == []:
        #         return int(tokens[i])
        #     try:
        #         if -200 <= int(tokens[i]) <= 200:
        #             stack.append(int(tokens[i]))
        #             flag += 1
        #     except ValueError:                
        #         if tokens[i] == "+":
        #             if flag >= 2:
        #                 result = stack.pop()
        #                 result = stack.pop() + result
        #             else:
        #                 result = stack.pop() + stack.pop()
        #             stack.append(result)
        #             flag -= 1
        #         elif tokens[i] == "-":
        #             if flag >= 2:
        #                 result = stack.pop()
        #                 result  = stack.pop() - result
        #             else:
        #                 result = stack.pop() - stack.pop()
        #             stack.append(result)
        #             flag -= 1
        #         elif tokens[i] == "/":
        #             if flag >= 2:
        #                 result = stack.pop()
        #                 result = int(stack.pop() / result)
        #             else:
        #                 result += int(stack.pop() / stack.pop())
        #             stack.append(result)
        #             flag -= 1
        #         elif tokens[i] == "*":
        #             if flag >= 2:
        #                 result = stack.pop()
        #                 result = stack.pop() * result
        #             else:
        #                 result = stack.pop() * stack.pop()
        #             stack.append(result)
        #             flag -= 1
        #     i += 1
        # return result
        
        # optimalised solution
        
        stack = []
        for i in range(len(tokens)):         
            if tokens[i] == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif tokens[i] == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif tokens[i] == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            elif tokens[i] == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
    
    # leetcode 22
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return
        
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0,0)
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


                