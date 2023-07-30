from typing import List

class Solution():
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dictionary_s = {}
        # dictionary_t = {}
        # if len(s) != len(t):
        #     return False
        # for i in range(len(s)):
        #     dictionary_s[s[i]] = dictionary_s.get(s[i], 0) + 1
        #     dictionary_t[t[i]] = dictionary_t.get(t[i], 0) + 1
        # if dictionary_s == dictionary_t:
        #     return True
        # return False
        
        # simpler way
        if sorted(s) == sorted(t):
            return True
        else:
            return False

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(0,len(nums)):
            result = target - nums[i]
            if(result in dictionary):
                return [dictionary[result], i]
            else:
                dictionary[nums[i]] = i

    def groupAnagrams(self, strs: List[str]):
        dictionary = {}
        for i in strs:
            letter_count = [0] * 26
            for j in i:
                letter_count[ord(j) - ord("a")] += 1
            if tuple(letter_count) not in dictionary:
                dictionary[tuple(letter_count)] = [i]
            else:
                dictionary[tuple(letter_count)].append(i)
        return list(dictionary.values())
               