class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0]*(max(costs)+1)
        for cost in costs:
            freq[cost]+=1
        ans = []
        for i in range(len(freq)):
            if freq[i]==0:
                continue
            ans.extend([i]*freq[i])
        count = 0
        for i in range(len(ans)):
            if coins<ans[i]:
                break
            coins-=ans[i]
            count+=1
        return count
