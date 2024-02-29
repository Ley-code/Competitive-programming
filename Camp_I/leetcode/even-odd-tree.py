# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        stack = deque([root])
        level = 0
        while stack:
            for i in range(len(stack)):
                if level%2==0:
                    if stack[i].val%2==0:
                        return False
                    if i>0:
                        if stack[i].val<=stack[i-1].val:
                            return False
                else:
                    if stack[i].val%2!=0:
                        return False
                    if i>0:
                        if stack[i].val>=stack[i-1].val:
                            return False                     
            for i in range(len(stack)):
                val = stack.popleft()
                if val.left:
                    stack.append(val.left)
                if val.right:
                    stack.append(val.right)
            level = not level
        return True