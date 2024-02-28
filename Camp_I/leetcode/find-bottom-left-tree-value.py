# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        mp = {}
        def dfs(node,r,c):
            nonlocal mp
            if not node:
                return
            dfs(node.left,r+1,c-1)
            if r not in mp:
                mp[r] = node.val
            dfs(node.right,r+1,c+1)
        dfs(root,0,0)
        res = 0
        maxi = -float('inf')
        for num in mp:
            if num>maxi:
                maxi = num
                res = mp[num]
        return res