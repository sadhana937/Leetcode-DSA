class Solution:
    def largestGoodInteger(self, num: str) -> str:
        pattern = ''
        for i in range(9, -1, -1):
            pattern = str(i) * 3
            if pattern in num:
                return pattern
        return ''
