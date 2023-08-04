from typing import List
import string
import collections

class Solution():
    # leetcode 217
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
    
    # leetcode 242
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

    # leetcode 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(0,len(nums)):
            result = target - nums[i]
            if(result in dictionary):
                return [dictionary[result], i]
            else:
                dictionary[nums[i]] = i

    # leetcode 49
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
    
    # leetcode 347
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1
        temp = sorted(dictionary, key=lambda k: dictionary[k], reverse=True)
        result = []
        for i in range(k):
            result.append(temp[i])      
        return result
    
    # leetcode 238
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dictionary = {}
        length = len(nums)
        prefix = [0] * length
        prefix.insert(0,1)
        postfix = [0] * length
        postfix.insert(length, 1)
        for i in range(length):
            prefix[i+1] = (nums[i]*prefix[i])
            postfix[length - i - 1] = (nums[length - 1 - i]*postfix[length - i])
        result = []
        for i in range(length):
            result.append(prefix[i]*postfix[i+1])
        return result
    
     
    # leetcode 271   
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        result = ""
        for i in range(len(strs)):
            if strs[i] == ":":
                result += ":"
            if i < (len(strs) - 1):
                result += strs[i] + ":;"
            else:
                result += strs[i]
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str: string):
        result = []
        result = str.split(":;")
        for i in range(len(result)):
            if result[i] == "::":
                result[i] = ":"
        return result
    
    # leetcode 1678
    def interpret(self, command: str) -> str:
        result = command.replace("()", "o")
        result = result.replace("(al)", "al")
        return result
    
    # leetcode 36
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row = collections.defaultdict(set)
        hash_col = collections.defaultdict(set)
        hash_squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in hash_row[r] or 
                    board[r][c] in hash_col[c] or
                    board[r][c] in hash_squares[r // 3, c // 3]):
                    return False
                hash_row[r].add(board[r][c])
                hash_col[c].add(board[r][c])
                hash_squares[(r // 3, c // 3)].add(board[r][c])
        return True
    
    # leetcode 2133
    def checkValid(self, matrix: List[List[int]]) -> bool:
        hash_row = collections.defaultdict(set)
        hash_col = collections.defaultdict(set)
        
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if (matrix[r][c] in hash_row[r] or
                    matrix[r][c] in hash_col[c]):
                    return False
                hash_row[r].add(matrix[r][c])
                hash_col[c].add(matrix[r][c])
        return True

    # leetcode 128
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(set(nums)) == 1:
        #     return 1
        # for i in range(len(nums)):
        #     if i == 0:
        #         prev = nums[i]
        #         count += 1
        #     else:
        #         if (nums[i] == (prev + 1)):
        #             prev = nums[i]
        #             count += 1
        #             if count > highest:
        #                 highest = count
        #         else:
        #             prev = nums[i]
        #             count = 1
        #             if count > highest:
        #                 highest = count
        # return highest
        
        # better way of doing things
        nums = set(nums)
        longest = 0
        length = 0
        for n in nums:
            if (n - 1) not in nums:
                length = 1
                while (n + 1) in nums:
                    length += 1
                    n += 1
                if length > longest:
                    longest = length
        return longest 