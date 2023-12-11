class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = defaultdict(int)
        n = len(arr)
        for i in arr:
            count[i] += 1
            if count[i] > (n // 4):
                return i
