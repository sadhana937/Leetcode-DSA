class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):

            height_difference = heights[i + 1] - heights[i]

            if height_difference < 0:
                continue

            bricks -= height_difference
            heapq.heappush(heap, -height_difference)
            
            if bricks < 0:
                ladders -= 1
                bricks += -heapq.heappop(heap)

            if ladders < 0:
                return i

        return len(heights) - 1
