class Solution:
    def totalMoney(self, n: int) -> int:
        iterations = n // 7
        additional_days = n % 7
        total_money = 0
        for i in range(iterations):
            total_money += sum(range(i + 1, i + 8))
        total_money += sum(range(iterations + 1, iterations + additional_days + 1))
        return total_money
