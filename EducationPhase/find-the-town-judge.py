class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        trusts = defaultdict(int)
        for x,y in trust:
            trusted[y] +=1
            trusts[x]+=1
        for i in range(1,n+1):
            if trusted[i] == n-1 and trusts[i] == 0:
                return i
        return -1

        
            
                    