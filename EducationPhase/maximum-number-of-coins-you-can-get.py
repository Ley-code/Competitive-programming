class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        mypile = 0
        piles.sort()
        count = 0
        for i in range(len(piles)-2,-1,-2):
            count+=1
            if count > len(piles)//3:
                break
            mypile+=piles[i]
        return mypile