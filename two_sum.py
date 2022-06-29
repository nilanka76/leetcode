# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i , j]

        # for i in range(0, len(nums)):
        #     num2 = target-nums[i]
        #     try:
        #         if num2 in nums:
        #             if nums[i] == num2:
        #                 nums[i] = None
        #             return [i, nums.index(num2)]
        #     except:
        #         continue        
 
        dicta = {}
        for i in range(len(nums)):
            num2 =  target - nums[i]
            if num2 in dicta:
                return [dicta[num2], i]
            dicta[nums[i]] = i

solution = Solution()
lista =[2,5,5,11]
target = 10
print(solution.twoSum(lista, target))