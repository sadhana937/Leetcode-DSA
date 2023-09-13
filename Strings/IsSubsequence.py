# Time complexity: O(n + m)
# Space complexity: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j, i = 0, 0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                j += 1
            i += 1
        return len(s) == j
