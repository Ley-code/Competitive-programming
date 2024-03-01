# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        maxsum = 0
        def traverse(root):
            nonlocal maxsum
            if not root: 
                return 1, 0, None, None
            ls, leftsum, minileft, maxileft = traverse(root.left)
            rs, rightsum, miniright, maxiright = traverse(root.right)
            if ((ls == 2 and maxileft < root.val) or ls == 1) and ((rs == 2 and miniright > root.val) or rs == 1):
                size = root.val + leftsum + rightsum
                maxsum = max(maxsum, size)
                return 2, size, (minileft if minileft is not None else root.val), (maxiright if maxiright is not None else root.val)
            return 0, None, None, None
        
        traverse(root)
        return maxsum