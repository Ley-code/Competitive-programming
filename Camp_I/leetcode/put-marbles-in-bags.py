class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        cuts = []
        for i in range(len(weights)-1):
            cuts.append(weights[i]+weights[i+1])
        cuts.sort()
        ans = 0
        n = len(cuts)
        for i in range(k-1):
            minimum=cuts[i]
            maximum=cuts[n-i-1]
            ans += maximum-minimum
        return ans