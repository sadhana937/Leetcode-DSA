class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = []
        for i in range(1, n + 1):
            nums.append(str(i))
        nums.sort()
        nums = [int(i) for i in nums]
        return nums
