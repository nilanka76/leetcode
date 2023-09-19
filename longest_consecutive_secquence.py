# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nset = set(nums)
        longest = 0
        
        for i in nums:
            if (i - 1) not in nset:
                length = 0
                while (i + length) in nset:
                    length += 1
                longest = max(longest, length)
        return longest