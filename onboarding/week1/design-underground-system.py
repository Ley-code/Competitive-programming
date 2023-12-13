class UndergroundSystem:

    def __init__(self):
        self.passengerId = {}
        self.destination = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengerId[id] = [stationName,t]
            
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.passengerId[id][0],stationName) in self.destination:
            self.destination[(self.passengerId[id][0],stationName)][0] += (t-self.passengerId[id][1])
            self.destination[(self.passengerId[id][0],stationName)][1] += 1
        else:
            self.destination[(self.passengerId[id][0],stationName)] = [t-self.passengerId[id][1],1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (self.destination[(startStation,endStation)][0]/self.destination[(startStation,endStation)][1])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)