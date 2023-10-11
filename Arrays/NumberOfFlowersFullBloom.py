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
            answer[i] = self.binarySearchRight(start, people[i]) - self.binarySearchLeft(end, people[i])

        return answer
    
    def binarySearchRight(self, arr, value):
        low = 0
        high = len(arr)
        while low < high:
            mid = low + (high - low) // 2
            if value < arr[mid]:
                high = mid
            else:
                low = mid + 1
        return low
    
    def binarySearchLeft(self, arr, value):
        low = 0
        high = len(arr)
        while low < high:
            mid = low + (high - low) // 2
            if value <= arr[mid]:
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

