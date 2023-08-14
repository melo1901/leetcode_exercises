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
    
    #leetcode 739
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # first solution, time O(n^2)
        
        # j = 0
        # result = 1
        # temp = 0
        # answer = []
        # for i in range(len(temperatures)):
        #     reverse_temp = temperatures[:j:-1]
        #     if i != len(temperatures) - 1:
        #         try:
        #             temp = reverse_temp.pop()
        #             while temp <= temperatures[i]:
        #                 result += 1
        #                 temp = reverse_temp.pop()
        #             answer.append(result)
        #         except IndexError:
        #             answer.append(0)
        #     else:
        #         answer.append(0)
        #     result = 1
        #     j += 1
        # return answer
        
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        return result
    
    # leetcode 1614
    def maxDepth(self, s: str) -> int:
        # dictionary solution
        
        # var = {
        #     "(": 0,
        #     "highest": 0
        #     }
        # for char in s:
        #     if char == "(":
        #         var["("] += 1
        #     elif char == ")":
        #         var["("] -= 1
        #     if var["("] > var["highest"]:
        #         var["highest"] = var["("]
                
        # return var["highest"]
        
        # stack solution
        
        stack = []
        result = 0
        for char in s:
            if len(stack) > result:
                result = len(stack)
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop()
                
        return result
    
    # leetcode 1021
    def removeOuterParentheses(self, s: str) -> str:
        # first working solution
        
        # flag = 0
        # stack = []
        # for i in range(len(s)):
        #     if flag == 0:
        #         stack.append([s[i], flag])
        #         flag += 1
        #     else:
        #         if s[i] == "(":
        #             flag += 1
        #             stack.append([s[i], flag])
        #         else:
        #             flag -= 1
        #             stack.append([s[i], flag])
        # str = ""
        # for item in stack:
        #     if item[1] > 0:
        #         str += item[0]
        # return str
        
        flag = 0
        stack = []
        for char in s:
            if flag == 0:
                stack.append(char)
                flag += 1
                stack.pop()
            else:
                if char == "(":
                    flag += 1
                    stack.append(char)
                else:
                    flag -= 1
                    stack.append(char)
                    if flag == 0:
                        stack.pop()
                        
        return ''.join(stack)
            
                
          
            
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


                