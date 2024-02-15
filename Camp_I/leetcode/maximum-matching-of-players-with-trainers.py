class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        match,l,r = 0,len(players)-1,len(trainers)-1
        while l>=0 and r>=0:
            if players[l]>trainers[r]:
                l-=1
            else:
                match+=1
                l-=1
                r-=1
        return match

        