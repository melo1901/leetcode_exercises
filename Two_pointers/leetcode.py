import re

class Solution():
    
    # leetcode 125
    def isPalindrome(self, s: str) -> bool:           
        s = re.sub(r'[\W_]', '', s.lower())
        return s == s[::-1]
        
        # version 2
        # s = ''.join(filter(str.isalnum, s))      
        # return s.lower() == s[::-1].lower()