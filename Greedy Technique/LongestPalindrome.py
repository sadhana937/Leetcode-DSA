class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        output = 0
        odd = False
        for i in count.values():
            if i % 2 == 0:
                output += i
            elif i % 2 == 1:
                odd = True
                output += (i - 1)
        if odd:
            output += 1
        return output
            
