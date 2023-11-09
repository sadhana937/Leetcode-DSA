class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = s[0]
        count = 0
        result = 0
        for i in s:
            if prev == i:
                count += 1
            else:
                prev = i
                count = 1
            result += count
        return result % (10 ** 9 + 7)
