class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        half_len = len(s) // 2
        first = s[:half_len]
        second = s[half_len: len(s)]
        count1 = 0
        count2 = 0
        for i in ['a', 'e', 'i', 'o', 'u']:
            count1 += first.count(i)
            count2 += second.count(i)
        return count1 == count2
        
