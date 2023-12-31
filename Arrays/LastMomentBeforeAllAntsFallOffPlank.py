class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_max = max(left) if left else 0
        right_max = n - min(right) if right else 0
        return max(left_max, right_max)

'''
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if len(left) == 0:
            return n - min(right)
        elif len(right) == 0:
            return max(left)
        else:
            max_left = max(left)
            max_right = n - min(right)
        return max_left if max_left > max_right else max_right
'''
