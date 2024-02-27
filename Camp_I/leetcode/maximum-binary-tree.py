# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(left,right):
            if left>right:
                return None
            mid = nums.index(max(nums[left:right+1]))
            curr = TreeNode(nums[mid])
            curr.left = divide(left,mid-1)
            curr.right = divide(mid+1,right)
            return curr
        return divide(0,len(nums)-1)