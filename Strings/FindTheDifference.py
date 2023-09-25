# Return the additional letter added to string t - using hash map
# n -> length of string t
# Time complexity: O(n)
# Space complexity: O(n)

class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_map = {}
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        for i in t:
            if i in hash_map and hash_map[i] > 0:
                hash_map[i] -= 1
            else:
                return i


# Time complexity: O(n)
# Spapce complexity: O(1)
class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i
