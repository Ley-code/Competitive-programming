# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sums = 0
        stack = []
        def recurse(node):
            nonlocal sums
            nonlocal stack
            if not node:
                return
            if not node.left and not node.right:
                res = ""
                stack.append(str(node.val))
                for i in range(len(stack)):
                    res+=stack[i]
                sums+=int(res)
                return
            stack.append(str(node.val))
            if node.left:
                recurse(node.left)
                stack.pop()
            if node.right:
                recurse(node.right)
                stack.pop()
            return
        recurse(root)
        return sums