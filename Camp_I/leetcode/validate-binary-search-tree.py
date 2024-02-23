# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(root,upper,lower):
            if not root:
                return True
            if lower<root.val<upper:
                return recurse(root.left,root.val,lower) and recurse(root.right,upper,root.val)
            else:
                return False    
        return recurse(root,float('inf'),-float('inf'))