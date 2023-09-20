#https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: 
            return 1
        lst = []
        i = 0
        j = 1
        while j < len(chars) :
            while (j < len(chars) and chars[i] == chars[j]):
                j += 1

            lst.append(chars[j-1])
            # print(i, j)
            n = j - i
            if(n >= 10):
                n = str(n)
                for i in n:
                    lst.append(i)
            elif(n > 1):
                lst.append(str(n))
            
            i = j
            j += 1

            if j == len(chars):
                lst.append(chars[j-1])
            # print(i, j)

        # print(lst)
        # print(chars)

        k = 0
        for ch in lst:
            chars.insert(k, ch)
            k += 1
        return len(lst)