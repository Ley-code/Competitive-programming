# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []
        if not root:
            return []
        while queue:
            temp = []
            for i in range(len(queue)):
                val = queue.popleft()
                temp.append(val.val)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            ans.append(temp)
        return ans
        