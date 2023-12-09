# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative approach
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root is None:
            return []
        cur = root
        while True:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            if not stack:
                break
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result

# Recurvise approach
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        if root.left:
            result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        if root.right:
            result.extend(self.inorderTraversal(root.right))
        return result
