# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # len1 = len(nums1)
        # len2 = len(nums2)
        # li = []
        # if len1 < len2:
        #     for i in nums1:
        #         if i in nums2:
        #             nums2.remove(i)
        #             li.append(i)
        # else:
        #     for i in nums2:
        #         if i in nums1:
        #             nums1.remove(i)
        #             li.append(i)
        # return li

        # c = collections.Counter(nums1) & collections.Counter(nums2)
        # print(c)
        # ans = []
        # for k, v in c.items():
        #     print(k, v)
        #     ans.extend([k] * v)
        # return ans

        hmap = {} 
        li = []
        for num in nums1:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
                
        for num in nums2:
            if num in hmap:
                if hmap[num] > 0:
                    li.append(num)
                    hmap[num] -= 1                  
        return li

solution = Solution()
lista = [4,9,5]
listb = [4,1,8,9,4]
print(solution.intersect(lista,listb))