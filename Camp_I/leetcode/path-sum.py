# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def backtrack(node,sums):
            if not node:
                return False
            if not node.left and not node.right:
                if sums+node.val == targetSum:
                    return True
                return False
            val = backtrack(node.left,sums+node.val) or backtrack(node.right,sums+node.val)
            return val
        return backtrack(root,0)