#Best time to buy and sell stock using kadane's algorithm
#Time complexity: O(n)
#Space complexity: O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_stockprice = prices[0]
        for i in range(1,len(prices)):
            max_profit = max(max_profit, prices[i] - min_stockprice) #compare the maximum profit with the generated profit
            min_stockprice = min(min_stockprice, prices[i])
        return max_profit
