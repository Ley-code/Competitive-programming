# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def fillarr(node):
            #nonlocal arr
            if not node:
                return
            fillarr(node.left)
            arr.append(node.val)
            fillarr(node.right)
        fillarr(root)
        def bbst(left,right):
            if left>right:
                return None
            mid = left + (right-left)//2
            curr  = TreeNode(arr[mid])
            curr.left = bbst(left,mid-1)
            curr.right = bbst(mid+1,right)
            return curr
        return bbst(0,len(arr)-1)
