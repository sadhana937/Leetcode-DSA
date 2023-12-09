# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative approach
class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        if root is None:
            return []
        cur = root
        while True:
            while cur is not None:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            
            if not stack:
                break
            
            cur = stack.pop()
            cur = cur.right
        
        return result

# Recursive approach
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return
        result.append(root.val)
        if root.left:
            result.extend(self.preorderTraversal(root.left))
        if root.right:
            result.extend(self.preorderTraversal(root.right))
        return result
