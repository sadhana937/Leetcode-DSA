# BRUTE FORCE
class Solution1:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            matches += n // 2
            if n % 2 != 0:
                n = (n // 2) + 1
            else:
                n = n // 2
        return matches

# To decide the winner n - 1 matches needs to be played
class Solution2:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
