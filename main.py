from Stack.leetcode import Solution
from Stack.leetcode import MinStack

target = 6
s = "([])"
strs = ["we", "say", ":", "yes"]
str = "we:;say:;;:;yes"
k = 2
command = "G()(al)"
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
numbers = [2,3,4]
target = 6
height = [4,2,3]
obj = MinStack()
obj.push(1)
obj.push(10)
print(obj.getMin())
#print(Solution().isValid(s))