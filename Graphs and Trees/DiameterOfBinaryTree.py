# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def heightOfTree(root):
            nonlocal diameter
            if not root:
                return 0
            left = heightOfTree(root.left)
            right = heightOfTree(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        diameter = 0
        heightOfTree(root)
        return diameter
