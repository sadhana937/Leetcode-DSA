class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        a_count = s.count('a')
        output = float("inf")

        for i in s:
            if i == 'a':
                a_count -= 1
            output = min(output, b_count + a_count)
            if i == 'b':
                b_count += 1
        return output
            
