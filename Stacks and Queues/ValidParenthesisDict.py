class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dictionary={'(':')','{':'}','[':']'}
        for i in s:
            if i in '({[':
                stack.append(i)
            elif not stack or i!=dictionary[stack.pop()]:
                return False
        return not stack
