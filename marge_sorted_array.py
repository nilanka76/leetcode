# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.
# nums2 has a length of n.
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[i + m] = nums2[i]
        # nums1.sort()

        while m!=0 and n!=0:
            if nums1[m-1]>nums2[n-1]:
                m-=1
                nums1[m+n] = nums1[m]
            else:
                n-=1
                nums1[m+n] = nums2[n]
                
        while n!=0:
            n-=1
            nums1[n] = nums2[n]

solution = Solution()
list1 = [-4,-1,0,3,16,0,0,0,0]
list2 = [-5,4,10,50]
solution.merge(list1, 5, list2, 4)
print(list1)