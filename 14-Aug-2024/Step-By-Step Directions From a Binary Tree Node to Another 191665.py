# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node,target,path):
            if not node:
                return ""
            if node.val == target:
                return path
            path.append('L')
            left = dfs(node.left,target, path)
            
            if left: return path
            path.pop()
            
            path.append('R')
            right = dfs(node.right,target, path)
            if right: return path
            path.pop()
            return ""
            
        start  = dfs(root,startValue,[])
        dest = dfs(root, destValue,[])
        n = len(start)
        m = len(dest)
        l,r= 0 , 0
        ans = []
        flag = False
        while l<n and r<m:
            if start[l] == dest[r]:
                l+=1
                r+=1
            else:
                ans.extend(['U']*(n-l))
                ans.extend(dest[r:])
                flag = True
                break
        if not flag:
            ans.extend(['U']*(n-l))
            ans.extend(dest[r:])
        return "".join(ans)    