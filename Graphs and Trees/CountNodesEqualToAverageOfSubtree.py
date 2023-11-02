# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def postorder(root):
            if not root:
                return (0, 0)
            left = postorder(root.left)
            right = postorder(root.right)
            nonlocal result
            total_sum = left[0] + right[0] + root.val
            total_count = 1 + left[1] + right[1]
            if root.val == (total_sum // total_count):
                result += 1
            return (total_sum, total_count)

        postorder(root)
        return result
