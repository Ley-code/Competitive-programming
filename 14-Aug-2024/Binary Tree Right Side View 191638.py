# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        ans = []
        if not root:
            return ans
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i==n-1:
                    ans.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
