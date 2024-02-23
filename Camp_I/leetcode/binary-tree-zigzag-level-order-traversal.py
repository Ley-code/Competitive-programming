# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        level = 0
        ans = []
        if not root:
            return []
        while queue:
            n = len(queue)
            currans = []
            for _ in range(n):
                curr = queue.popleft()
                currans.append(curr.val)
                if curr.left:    
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level%2==0:
                ans.append(currans)
            else:
                ans.append(currans[::-1])
            level += 1
        return ans