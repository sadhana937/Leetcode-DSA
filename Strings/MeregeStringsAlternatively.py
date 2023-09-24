# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        m = len(word1)
        n = len(word2)
        result = []
        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1
        return "".join(result)
