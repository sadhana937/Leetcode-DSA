class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minspeed = 1
        maxspeed = max(piles)

        while minspeed < maxspeed:
            mid = minspeed + (maxspeed - minspeed) // 2
            curhours = 0
            for i in piles:
                curhours += i // mid
                if i % mid != 0:
                    curhours += 1
            if curhours <= h:
                maxspeed = mid
            else:
                minspeed = mid + 1
        return minspeed

