class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        nradiant = senate.count("R")
        ndire = senate.count("D")
        haveR = 0
        haveD = 0
        poppedR = 0
        poppedD = 0
        queue = deque(list(senate))
        l = 0
        while poppedR != nradiant and poppedD!=ndire:
            if queue[l] == "R" and haveD:
                poppedR+=1
                haveD-=1
            elif queue[l] == "R" and not haveD:
                haveR+=1
                queue.append("R")
            elif queue[l] == "D" and haveR:
                poppedD+=1
                haveR-=1
            elif queue[l] == "D" and not haveR:
                haveD+=1
                queue.append("D")
            l+=1
        return "Radiant" if poppedD==ndire else "Dire"
            