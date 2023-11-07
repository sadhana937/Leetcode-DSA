# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = []
        count = 0
        n = len(dist)
        for i in range(n):
            arrival.append(dist[i] / speed[i])
        arrival.sort()
        for i in range(n):
            if i < arrival[i]:
                count += 1
            else:
                break
        
        return count
