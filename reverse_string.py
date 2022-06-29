class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time complexity O(n)
        # for i in range(len(s)):
        #     s.append(s.pop(len(s) - 1 - i))
        
        # Time complexity O(n/2)
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)- 1 - i]
            s[len(s)- 1 - i] = temp

solution = Solution()
s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)