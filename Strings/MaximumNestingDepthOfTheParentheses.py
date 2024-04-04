class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        count = 0
        for i in s:
            if i == '(':
                count += 1
                max_count = max(max_count, count)
            elif i == ')':
                count -= 1
        return max_count
