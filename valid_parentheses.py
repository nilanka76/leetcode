# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#           Open brackets must be closed by the same type of brackets.
#           Open brackets must be closed in the correct order.
# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref ={")":"(", "}":"{", "]":"["}
        for i in s:
            if i in ref:
                if stack == [] or ref[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        if s != "" and stack == []:
            return True  
        return False

solution = Solution()
s = "()[{}]"
print(solution.isValid(s))