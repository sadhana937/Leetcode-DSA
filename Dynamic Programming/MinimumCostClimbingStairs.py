# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        C = len(cost)
        next_cost = second_next_cost = 0
        for i in range(C - 1, -1, -1):
            current_cost = cost[i] + min(next_cost, second_next_cost)
            second_next_cost = next_cost
            next_cost = current_cost
        return min(next_cost, second_next_cost)
