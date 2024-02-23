# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxval = 0
        def recurse(node):
            leftval = [float('inf'),-float('inf')]
            rightval = [float('inf'),-float('inf')]
            nonlocal maxval
            if not node.left and not node.right:
                return [node.val,node.val]
            if node.left:
                leftval = recurse(node.left)
            if node.right:
                rightval = recurse(node.right)
            maxi = max(leftval[1],rightval[1])
            mini = min(leftval[0],rightval[0])
            maxval = max(maxval,node.val-mini,maxi-node.val)
            return [min(mini,node.val),max(maxi,node.val)]
        val = recurse(root)
        return maxval
                
            