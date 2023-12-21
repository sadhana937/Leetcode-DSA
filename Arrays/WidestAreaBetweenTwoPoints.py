class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        points.sort(key=lambda point: point[0])
        max_dist = 0
        for i in range(1, len(points)):
            cur_dist = points[i][0] - points[i - 1][0]
            max_dist = max(max_dist, cur_dist)
        return max_dist
