class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 2
        cur = max(arr[0], arr[1])
        win = 1
        while win < k and i < len(arr):
            if arr[i] > cur:
                cur = arr[i]
                win = 1
            else:
                win += 1
            i += 1
        return cur
