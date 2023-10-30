class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        n = len(arr)
        for i in range(n):
            arr[i] = bin(arr[i])
        arr.sort(key = lambda x : x.count('1'))
        for i in range(n):
            arr[i] = int(arr[i], 2)
        return arr
        
