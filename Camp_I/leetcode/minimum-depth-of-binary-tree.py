# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        miniD = float('inf')
        def dfs(node,depth):
            nonlocal miniD
            if not node:
                return
            if not node.left and not node.right:
                miniD = min(miniD,depth+1)
                return
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return miniD if miniD!=float('inf') else 0
