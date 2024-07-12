class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        output = 0
        if x > y:
            first, second, max_val, min_val = 'a', 'b', x, y
        else:
            first, second, max_val, min_val = 'b', 'a', y, x

        for i in s:
            if i == first:
                stack.append(first)
            elif i == second and stack and stack[-1] == first:
                    output += max_val
                    stack.pop()
            else:
                stack.append(i)

        i = 0
        while i < len(stack) - 1:
            if stack[i] == second and stack[i + 1] == first:
                stack.pop(i)
                stack.pop(i)
                i -= 1
                output += min_val
            else:
                i += 1

        return output


        
                        

