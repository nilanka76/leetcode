# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        lst = list(magazine)
        for i in ransomNote:
            try:
                lst.remove(i)
            except:
                return False
        return True
solution = Solution
ransomNote = "aa"
magazine = "aab"
print(solution.canConstruct(ransomNote, magazine))