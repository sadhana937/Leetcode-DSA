class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequence = '123456789'
        output = []
        l = len(str(low))
        h = len(str(high))
        for i in range(l, h + 1):
            for j in range(10 - i):
                new = int(sequence[j: j + i])
                if  low <= new <= high:
                    output.append(new)
        return output
