class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        unique = set(s)
        for i in range(len(unique)):
            char = unique.pop()
            if s.count(char) != t.count(char):
                return False
        return True
        
