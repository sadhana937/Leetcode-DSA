class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        output = 0
        for i in range(n):
            if grumpy[i] == 0:
                output += customers[i]
                customers[i] = 0

        max_unsatisfied = 0
        for i in range(n):
            max_unsatisfied = max(max_unsatisfied, sum(customers[i:i + minutes]))
        
        return max_unsatisfied + output
