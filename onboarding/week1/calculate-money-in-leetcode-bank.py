class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        startweek = 0
        week = n//7
        leftoverdays = n%7
        while startweek < week:
            for j in range(1,8):
                total+= (j+startweek)
            startweek+=1
        for k in range(1,leftoverdays+1):
            total+=(startweek+k)
        return total
