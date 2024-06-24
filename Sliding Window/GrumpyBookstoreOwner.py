# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        output = 0
        for i in range(n):
            if grumpy[i] == 0:
                output += customers[i]
                customers[i] = 0

        current_unsatisfied = sum(customers[:minutes])
        max_unsatisfied = current_unsatisfied

        for i in range(minutes, n):
            current_unsatisfied += customers[i] - customers[i - minutes]
            max_unsatisfied = max(max_unsatisfied, current_unsatisfied)
        
        return max_unsatisfied + output
