class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c ** 0.5)
        while a <= b:
            temp = a ** 2 + b ** 2
            if temp == c:
                return True
            elif temp > c:
                b -= 1
            else:
                a += 1
        return False
