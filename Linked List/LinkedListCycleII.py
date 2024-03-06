# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = -1
        while head is not None:
            pos += 1
            if head.val == float('inf'):
                return head
            else:
                head.val = float('inf')                     
                head = head.next
        return None
