# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        indegree = {chr(i):0 for i in range(97,97+K)}
        arr = alien_dict
        
        for i in range(N-1):
            n = len(alien_dict[i])
            m = len(alien_dict[i+1])
            l = 0
            while l<n and l<m:
                if arr[i][l]==arr[i+1][l]:
                    l+=1
                else:
                    graph[arr[i][l]].append(arr[i+1][l])
                    indegree[arr[i+1][l]]+=1
                    break
        q = deque([])
        for char in indegree:
            if indegree[char]==0:
                q.append(char)
        
        ans = ""
        while q:
            char = q.popleft()
            ans+=char
            for nei in graph[char]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return ans