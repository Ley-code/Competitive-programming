class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        maxscore,score = 0,0
        l,r = 0,len(tokens)-1
        tokens.sort()
        while l<=r:
            flag1 = False
            if tokens[l]<=power:
                score+=1
                power-=tokens[l]
                flag1 = True
                l+=1
            else:
                if score:
                    score-=1
                    power+=tokens[r]
                    flag1 = True
                    r-=1
            if not flag1:
                break
            maxscore = max(score,maxscore)
        return maxscore
