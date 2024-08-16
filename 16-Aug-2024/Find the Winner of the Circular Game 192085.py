# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list_n = [i for i in range(1,n+1)]
        l = 0
        while len(list_n)>1:
            l+=(k-1)
            if l>=len(list_n):
                l = l%len(list_n)
            del list_n[l] 
        return list_n[0]