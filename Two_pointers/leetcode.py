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
            elif numbers[i] + numbers[j] < target:
                i += 1
        return [i + 1, j + 1]   
    
    # leetcode 15
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:  
        # first working version
        # nums = sorted(nums)
        # result = []
        # for x in range(len(nums) - 1):
        #     i = x
        #     z = x
        #     j = i + 1
        #     k = (len(nums) - 1)
        #     while(z < (len(nums) - 1) and i != j and i != k and j != k):
        #         if(i != j and i != k and j != k):
        #             if((nums[i] + nums[j] + nums[k]) == 0):
        #                 if(([nums[i], nums[j], nums[k]] not in result)):
        #                     result.append([nums[i], nums[j], nums[k]])
        #                 k -= 1
        #                 j = x + 1
        #                 z = x
                        
        #                 while j < k and nums[j - 1] == nums[j]:
        #                     j += 1
        #                 while j < k and nums[k + 1] == nums[k]:
        #                     k -= 1
        #             elif(nums[i] + nums[j] + nums[k] > 0):
        #                 k -= 1
        #             elif(nums[i] + nums[j] + nums[k] < 0):
        #                 j += 1
        # return result
    
        # optimalised first verison    
        nums.sort()
        result = []
        n = len(nums)
        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            i = x
            j = i + 1
            k = (n - 1)
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if(sum == 0):
                    result.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                elif(sum > 0):
                    k -= 1
                elif(sum < 0):
                    j += 1
        return result