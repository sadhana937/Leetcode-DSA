# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        output = [[-1] * n for _ in range(m)]
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        cur = head
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                if cur:
                    output[top][i] = cur.val
                    cur = cur.next
                else:
                    break
            top += 1

            for i in range(top, bottom + 1):
                if cur:
                    output[i][right] = cur.val
                    cur = cur.next
                else:
                    break
            right -= 1
        
            for i in range(right, left - 1, -1):
                if cur:
                    output[bottom][i] = cur.val
                    cur = cur.next
                else:
                    break
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                if cur:
                    output[i][left] = cur.val
                    cur = cur.next
                else:
                    break
            left += 1
        return output
