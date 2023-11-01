# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        result = []

        def mode(root):
            nonlocal count
            if not root:
                return
            count[root.val] += 1
            mode(root.left)
            mode(root.right)

        mode(root)
        max_occurrence = max(count.values())

        ans = [i for i in count if count[i] == max_occurrence]
        
        return ans
