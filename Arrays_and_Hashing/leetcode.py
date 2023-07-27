class Solution(object):
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
        dictionary_s = {}
        dictionary_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dictionary_s[s[i]] = dictionary_s.get(s[i], 0) + 1
            dictionary_t[t[i]] = dictionary_t.get(t[i], 0) + 1
        if dictionary_s == dictionary_t:
            return True
        return False

            
            