# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Space Complexity: O(1)
class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head is not None:
            if head.val == float('inf'):
                return True
            else:
                head.val = float('inf')                     
                head = head.next
        return False

# Space Complexity: O(n)
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head is not None:
            if head not in visited:
                visited.add(head)
                head = head.next
            else:
                return True
        return False
