# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = [nums[-1]]
        res = []
        i = 1
        j = len(nums)-2
        while i < len(nums):
            prefix.append(prefix[i-1]*nums[i])
            i += 1
            
        while j >= 0:
            postfix.insert(0, postfix[0]*nums[j])
            j -= 1

        res.append(postfix[1])

        for i in range(1,len(nums)-1):
            res.append(prefix[i-1] * postfix[i+1])

        res.append(prefix[len(nums)-2])
        return res