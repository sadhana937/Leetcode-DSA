# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# One pass
class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        slow = ListNode(0, head)
        result = slow  
        index = 1
        while head:
            if index >= (n + 1):
                slow = slow.next
            head = head.next
            index += 1

        slow.next = slow.next.next
        return result.next


# Two pass 
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
          
        slow.next = slow.next.next
        return head
