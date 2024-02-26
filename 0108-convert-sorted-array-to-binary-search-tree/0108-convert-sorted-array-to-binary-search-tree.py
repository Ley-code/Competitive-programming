# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def backtrack(arr):
            if len(arr)==1:
                return TreeNode(arr[0])
            if len(arr)==0:
                return None
            mid = len(arr)//2
            curr = TreeNode(arr[mid])
            curr.left = backtrack(arr[:mid])
            curr.right = backtrack(arr[mid+1:])
            return curr
        return backtrack(nums)