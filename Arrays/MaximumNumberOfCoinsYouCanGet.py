class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        answer = 0
        i = len(piles) - 2
        j = 0
        while j < i:
            answer += piles[i]
            i -= 2
            j += 1
        return answer
