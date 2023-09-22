# Finding the digital root
# Time complexity: O(1)
# Space complexity: O(1)

class Solution1:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (9 if num % 9 == 0 else num % 9) 

# Time complexity: O(n)
# Space complexity: O(1)
class Solution2:
    def addDigits(self, num: int) -> int:
        digital_root = 0
        while num > 9:
            while num > 0:
                digital_root += num % 10
                num = num // 10
            num = digital_root
            digital_root = 0
        return num
