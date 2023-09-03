class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]
        for i in range(n):
            if s[i] in '({[':
                stack.append(s[i])
            elif s[i] in ')}]':
                if not stack:
                    return False
                y=stack.pop()
                if y=='(' and s[i]!=')':
                    return False
                if y=='{' and s[i]!='}':
                    return False
                if y=='[' and s[i]!=']':
                    return False
        return not stack
