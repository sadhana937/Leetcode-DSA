class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] * n
        for i, j in roads:
            indegree[j] += 1
            indegree[i] += 1

        heap = []
        for i, val in enumerate(indegree):
            heapq.heappush(heap, [val, i])

        weights = [0] * n
        count = 1
        while heap:
            weights[heapq.heappop(heap)[1]] = count
            count += 1
            
        summ = 0
        for i, j in roads:
            summ += (weights[i] + weights[j])
        return summ
