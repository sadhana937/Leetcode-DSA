class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        count = len(t) 
        s = list(s)
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                count -= 1
                j += 1
            i += 1
        
        return count

