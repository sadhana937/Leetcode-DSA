# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            if cur.val == 0:
                prev = cur
                cur_val = 0
                cur = cur.next
                while cur.val != 0:
                    cur_val += cur.val
                    cur = cur.next
                prev.val = cur_val
                prev.next = cur
            else:
                cur = cur.next
                
        prev.next = None
        
        return head
