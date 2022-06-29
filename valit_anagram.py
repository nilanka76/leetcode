# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False
        sdic, tdic = {}, {}
        for i in range(len(s)):
            sdic[s[i]] = sdic.get(s[i], 0) + 1
            tdic[t[i]] = tdic.get(t[i], 0) + 1
        for i in tdic:
            if tdic[i] != sdic.get(i, 0):
                return False
        return True
solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.isAnagram(s, t))