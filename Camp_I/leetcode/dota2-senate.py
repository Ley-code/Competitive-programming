class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rqueue = deque()
        Dqueue = deque()
        lastidx = len(senate)
        for i in range(lastidx):
            if senate[i] == "R":
                Rqueue.append(i)
            else:
                Dqueue.append(i)
        while Rqueue and Dqueue:
            if Rqueue[0]<Dqueue[0]:
                Dqueue.popleft()
                Rqueue.popleft()
                Rqueue.append(lastidx)
                lastidx+=1
            else:
                Dqueue.popleft()
                Rqueue.popleft()
                Dqueue.append(lastidx)
                lastidx+=1
        return "Radiant" if Rqueue else "Dire"
            