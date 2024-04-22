# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [i for i in range(len(quiet))]
        graph = defaultdict(list)
        indegree = {i:0 for i in range(len(quiet))}
        for x,y in richer:
            graph[x].append(y)
            indegree[y]+=1
        q = deque([num for num in indegree if indegree[num]==0])
        while q:
            num = q.popleft()
            for nei in graph[num]:
                if quiet[ans[num]]<quiet[ans[nei]]:
                    ans[nei] = ans[num]
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return ans