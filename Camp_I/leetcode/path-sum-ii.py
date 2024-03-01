# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def backtrack(paths,node,sums):
            if not node:
                return
            if not node.left and not node.right:
                if sums+node.val==targetSum:
                    paths.append(node.val)
                    ans.append(paths[:])
                    paths.pop()
                return
            paths.append(node.val)
            backtrack(paths,node.left,sums+node.val)
            backtrack(paths,node.right,sums+node.val)
            paths.pop()
        backtrack([],root,0)
        return ans
