# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        maxval = 0
        def recurse(node,low,high):
            nonlocal maxval
            if not node:
                return
            if node.val<low:
                recurse(node.right,low,high)
            if node.val>high:
                recurse(node.left,low,high)
            if low<=node.val and high>=node.val:
                recurse(node.left,low,high)
                recurse(node.right,low,high)
                maxval += node.val
            return
        recurse(root,low,high)
        return maxval