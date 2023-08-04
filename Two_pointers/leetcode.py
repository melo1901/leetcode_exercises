import re

class Solution():
    
    # leetcode 125
    def isPalindrome(self, s: str) -> bool:           
        s = re.sub(r'[\W_]', '', s.lower())
        if s == s[::-1]:
            return True
        else:
            return False
        
        # version 2
        # s = ''.join(filter(str.isalnum, s))      
        # if s.lower() == s[::-1].lower():
        #     return True
        # else:
        #     return False