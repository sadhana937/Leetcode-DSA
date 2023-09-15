# Greatest Common Divisor of Str=ings - Brute Force
# Time complexity: O(min(m,n).(m+n))
# Space complexity: O(min(m,n)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len, str2_len = len(str1), len(str2)
        
        for i in range(min(str1_len,str2_len),0,-1):
            if not (str1_len % i or str2_len % i): # if the strings are divisible the base string length
                x = str1[:i] # x -> base string
                len1 = str1_len // i
                len2 = str2_len // i
                if str1 == len1 * x and str2 == len2 * x:
                    return x
        return ''            
