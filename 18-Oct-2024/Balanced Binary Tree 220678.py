# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def recurse(node):
            nonlocal flag
            if not node:
                return 0
            
            left = recurse(node.left)
            right = recurse(node.right)

            if abs(left-right)>1:
                flag = False
            return max(left,right)+1
        recurse(root)
        return flag
            