# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False] * n
        max_candies = max(candies)
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True
        return result
