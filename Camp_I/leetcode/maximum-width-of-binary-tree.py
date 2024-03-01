# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mp = {}
        def dfs(node,r,c):
            nonlocal maxlen
            nonlocal mp
            if not node:
                return
            dfs(node.left,r+1,2*c)
            if r not in mp:
                mp[r] = [c,c]
            dfs(node.right,r+1,(2*c)+1)
            if r in mp:
                val = mp[r]
                mini  = min(val[0],c)
                maxi = max(val[1],c)
                mp[r] = [mini,maxi]
        
        maxlen = 0
        dfs(root,0,0)
        for row in mp:
            maxlen = max(maxlen,mp[row][1]-mp[row][0]+1)
        return maxlen