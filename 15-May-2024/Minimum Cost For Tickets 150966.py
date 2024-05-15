# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(i,valid):
            if i>=len(days):
                return 0
            if (i,valid) in memo:
                return memo[(i,valid)]
            if days[i]>valid:
                onepass = dp(i+1,days[i]+0)+costs[0]
                sevpass = dp(i+1,days[i]+6)+costs[1]
                monpass  = dp(i+1,days[i]+29)+costs[2]
                memo[(i,valid)] = min(onepass,sevpass,monpass)
                return memo[(i,valid)]
            else:
                return dp(i+1,valid)
        return dp(0,0)
            