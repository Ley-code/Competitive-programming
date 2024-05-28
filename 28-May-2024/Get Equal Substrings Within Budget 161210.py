# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = []
        for i in range(len(s)):
            costs.append(abs(ord(s[i])-ord(t[i])))
        presum = [0]
        for cost in costs:
            presum.append(presum[-1]+cost)
        l = 0
        maxlen = 0
        for r in range(len(presum)):
            cost = presum[r] - presum[l]
            while l<len(presum) and cost>maxCost:
                cost-=presum[l]
                l+=1
            maxlen = max(maxlen,r-l)
        return maxlen