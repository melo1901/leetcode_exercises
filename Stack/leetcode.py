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
            
                