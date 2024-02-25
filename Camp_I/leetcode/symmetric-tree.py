# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftnode = root.left
        rightnode = root.right
        arr1 = []
        arr2 = []
        def recurse(node,arr):
            if not node:
                arr.append(-1)
                return 
            arr.append(node.val)
            recurse(node.left,arr)
            recurse(node.right,arr)
            return
        
        def recurse1(node,arr):
            if not node:
                arr.append(-1)
                return 
            arr.append(node.val)
            recurse1(node.right,arr)
            recurse1(node.left,arr)
            return
        recurse(leftnode,arr1)
        recurse1(rightnode,arr2)
        if len(arr1)!=len(arr2):
            return False
        for i in range(len(arr1)):
            if arr1[i]!=arr2[i]:
                return False
        return True