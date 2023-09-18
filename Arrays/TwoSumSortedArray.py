# Two sum - Input array is sorted (Two pointer method)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            x = numbers[i] + numbers[j]
            if x > target:
                j -= 1
            elif x < target:
                i += 1
            else:
                return [i + 1, j + 1]
