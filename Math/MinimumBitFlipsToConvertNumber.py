class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin1 = str(format(start, '032b'))
        bin2 = str(format(goal, '032b'))
        count = 0
        i = 31
        while i > -1:
            if bin1[i] != bin2[i]:
                count += 1
            i -= 1

        return count


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        count = 0
        while xor:
            count += xor & 1
            xor >>= 1
        return count

  class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        return xor.bit_count()
