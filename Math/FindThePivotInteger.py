class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return n
        left_sum = 0
        right_sum = sum(range(1, n + 1))

        for i in range(1, n + 1):
            left_sum += i
            right_sum -= i - 1
            if left_sum == right_sum:
                return i
        return -1
