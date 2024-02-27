# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def pathSum(root):
            if not root:
                return 0
            left = pathSum(root.left)
            right = pathSum(root.right)
            self.totalSum = max(self.totalSum, left + right + root.val)
            return max(left + root.val, right + root.val, 0)

        self.totalSum = float("-inf")
        pathSum(root)
        return self.totalSum
