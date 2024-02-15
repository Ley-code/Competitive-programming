class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target!=1:
            if maxDoubles and target%2==0:
                maxDoubles-=1
                count+=1
                target = target//2
            elif maxDoubles and target%2!=0:
                count+=2
                maxDoubles-=1
                target = (target-1)//2
            else:
                count+= target-1
                target = 1
        return count
