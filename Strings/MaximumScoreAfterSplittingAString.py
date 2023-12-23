class Solution:
    def maxScore(self, s: str) -> int:
        count1 = s.count('1')
        count0 = 0
        ans = 0
        for i in range(len(s) - 1):
            if s[i] == '1':
                count1 -= 1
            else:
                count0 += 1
            ans = max(ans, count1 + count0)

        return ans
