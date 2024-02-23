# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freqmap = defaultdict(int)
        def recurse(node):
            if not node:
                return
            freqmap[node.val] +=1
            recurse(node.left)
            recurse(node.right)
            return
        recurse(root)
        ans = []
        maxval = max(freqmap.values())
        for key in freqmap:
            if freqmap[key] == maxval:
                ans.append(key)
        return ans
            