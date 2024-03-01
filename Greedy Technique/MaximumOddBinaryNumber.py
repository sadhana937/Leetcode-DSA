class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        numberOfOnes = s.count('1')
        numberOfZeroes = len(s) - numberOfOnes
        return '1' * (numberOfOnes - 1) + '0' * (numberOfZeroes) + '1'
