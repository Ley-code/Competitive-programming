# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        result = []
        ablosers = set()
        for win,los in matches:
            winners.add(win)
            if los in losers:
                ablosers.add(los)
            losers.add(los)
        answer1 = sorted(list(winners - losers))
        answer2 = sorted(list(losers - ablosers))
      
        return[answer1,answer2]