'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        new = str(bin(n))
        count = 0
        for i in new:
            if i == '1':
                count += 1
        return count
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        new = str(bin(n))
        return new.count('1')
