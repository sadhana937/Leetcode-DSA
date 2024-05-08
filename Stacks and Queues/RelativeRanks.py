class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        count = 1
        medals = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}

        for i, val in enumerate(score):
            heapq.heappush(heap, [-val, i])

        while heap:
            _ , indx = heapq.heappop(heap)
            if count <= 3:
                score[indx] = medals[count]
            else:
                score[indx] = str(count)
            count += 1
               
        return score
        
