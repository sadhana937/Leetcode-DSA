# Time Complexity: O(log(m * n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_element = matrix[mid // cols][mid % cols]

            if mid_element == target:
                return True
            elif mid_element < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# Time Complexity: O(m * log(n))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in range(i[0], i[-1] + 1):
                left = 0
                right = len(i) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if target == i[mid]:
                        return True
                    elif target < i[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                continue
        return False
