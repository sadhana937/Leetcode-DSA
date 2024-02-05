class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
