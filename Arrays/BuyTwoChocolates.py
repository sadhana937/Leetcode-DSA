class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        money_left = money
        a = min(prices)
        money_left -= a
        prices.remove(a)
        a = min(prices)
        money_left -= a
        if money_left < 0:
            return money
        else:
            return money_left
