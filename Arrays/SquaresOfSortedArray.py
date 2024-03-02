class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right, index = 0, n - 1, n - 1
        
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                result[index] = left_square
                left += 1
            else:
                result[index] = right_square
                right -= 1
            index -= 1
        
        return result


class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            nums[i] = nums[i] * nums[i]
            nums[j] = nums[j] * nums[j]
            i += 1
            j -= 1
        middleIndex = n // 2
        if n % 2 != 0:
            nums[middleIndex] = nums[middleIndex] * nums[middleIndex]
        return sorted(nums)

class Solution3:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        return sorted(nums)
