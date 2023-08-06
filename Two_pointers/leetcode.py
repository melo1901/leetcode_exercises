import re
from typing import List

class Solution():
    
    # leetcode 125
    def isPalindrome(self, s: str) -> bool:           
        s = re.sub(r'[\W_]', '', s.lower())
        return s == s[::-1]
        
        # version 2
        # s = ''.join(filter(str.isalnum, s))      
        # return s.lower() == s[::-1].lower()
        
    # leetcode 167
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while(numbers[i] + numbers[j] != target):
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        return [i + 1, j + 1]     