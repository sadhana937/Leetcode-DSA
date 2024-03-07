# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        # finding the head of the second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing the second half of the list
        cur = slow
        prev = None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        # finding max twin sum
        max_sum = float('-inf')
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            prev = prev.next
            head = head.next

        return max_sum
