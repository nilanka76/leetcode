# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        # setn = set(nums)
        # print(setn)
        # print(nums)

        # if nums == list(setn):
        #     return False
        # else:
        #     return True

        n_list = []
        for num in nums:    
            if num in n_list:  
                return True
            else:
                n_list.append(num)  
            print(n_list)  
        return False
        
solution = Solution()
print(solution.containsDuplicate([1,2,3,4,4,5,6]))