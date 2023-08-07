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
    
    # leetcode 11
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0
        highest = 0
        while i < j:
            area = j - i
            if height[i] > height[j]:
                area = area * height[j]
                j -= 1
                if area > highest:
                    highest = area
            elif height[i] < height[j]:
                area = area * height[i]
                i += 1
                if area > highest:
                    highest = area
            elif height[i] == height[j]:
                area = area * height[i]
                i += 1
                if area > highest:
                    highest = area
        return highest

    # leetcode 42
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        trapped = 0
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                trapped += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                trapped += max_r - height[r]
        return trapped
            
            
            