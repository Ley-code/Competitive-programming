class Solution:
    def judgeCircle(self, moves: str) -> bool:
        verticalpos = 0
        horizontalpos = 0
        for c in moves:
            if c == "U":
                verticalpos+=1
            elif c== "D":
                verticalpos-=1
            elif c == "L":
                horizontalpos+=1
            else:
                horizontalpos-=1
        if verticalpos or horizontalpos:
            return False
        return True