# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i ==len(j) or strs[0][i] != j[i]:
                    return res
            res += strs[0][i]
        return res
soluton = Solution()
strs = ["flower","flow","flight"]
print(soluton.longestCommonPrefix(strs))