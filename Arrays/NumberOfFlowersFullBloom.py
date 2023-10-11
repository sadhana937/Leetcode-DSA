'''
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        F = len(flowers)
        P = len(people)
        answer = [0] * P
        start = [flowers[i][0] for i in range(F)]
        start.sort()
        end = [flowers[i][1] for i in range(F)]
        end.sort()
        for i in range(P):
            answer[i] = self.binarySearch(start, people[i], False) - self.binarySearch(end, people[i], True)
        return answer
    
    def binarySearch(self, arr, value, leftBias):
        low = 0
        high = len(arr)
        while low < high:
            mid = low + (high - low) // 2
            if value < arr[mid] or (leftBias and value == arr[mid]):
                high = mid
            else:
                low = mid + 1
        return low
'''
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        F = len(flowers)
        P = len(people)
        answer = [0] * P
        start = [flowers[i][0] for i in range(F)]
        start.sort()
        end = [flowers[i][1] for i in range(F)]
        end.sort()
        for i in range(P):
            answer[i] = bisect_right(start, people[i]) - bisect_left(end, people[i])
        return answer

