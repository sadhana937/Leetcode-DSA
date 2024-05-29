class Solution1:
    def numSteps(self, s: str) -> int:
        s = list(s)
        count = 0
        while len(s) > 1:
            if s[-1] == '0':
                s.pop()
            else:
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                if i >= 0:
                    s[i] = '1'
                else:
                    s.insert(0, '1')
            count += 1
        return count
            
class Solution2:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        count = 0
        while num > 1:
            if num % 2 == 0:
                num = num // 2
                count += 1
            if num == 1:
                return count
            if num % 2 == 1:
                num += 1
                count += 1
        return count
        
            
        
