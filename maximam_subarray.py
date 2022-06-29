# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currentSum = 0
        maxSum = nums[0]
        for i in nums:
            currentSum += i
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxSum

solution = Solution()
lista = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(lista))