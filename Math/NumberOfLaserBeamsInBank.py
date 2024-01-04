class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = [0] * len(bank)
        for i in range(len(bank)):
            count[i] = bank[i].count('1')
        output = 0
        prev = 0
        for i in count:
            if i != 0:
                output += prev * i
                prev = i
        return output
