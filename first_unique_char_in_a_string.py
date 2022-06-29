# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.
# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int: 
        hashMap = {}
        for i in s:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 0
        for values in hashMap:
            if hashMap[values] == 0:
                return s.index(values)
        return -1
s = "loveleetcode"
solution = Solution()
print(solution.firstUniqChar(s))