# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        # s = list(s)
        # lst = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M": 1000,
        #        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        # num = 0
        # def toInt(num: int, s: list, lst: dict):
        #     num += lst[s[0]+ s[1]]
        #     s.remove(s[0])
        #     s.remove(s[0])
        #     return(num)
        # while s:
        #     try:
        #         if (s[0] == "C") and (s[1] == "D" or s[1] == "M"):
        #             num = toInt(num, s, lst)
        #         elif (s[0] == "X") and (s[1] == "L" or s[1] == "C"):
        #             num = toInt(num, s, lst)
        #         elif (s[0] == "I") and (s[1] == "V" or s[1] == "X"):
        #             num = toInt(num, s, lst)
        #         else:
        #             num += lst[s[0]]
        #             s.remove(s[0])
        #     except:
        #         num += lst[s[0]]
        #         s.remove(s[0])
        # return num

        lst={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s=s.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX').replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
        num=0
        for i in s:
            num+=lst[i]
        return num

solution = Solution()
s = "MCMXCIV"
print(solution.romanToInt(s))