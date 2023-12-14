class FrequencyTracker:

    def __init__(self):
        self.dict = Counter()
        self.dict2 = Counter()

    def add(self, number: int) -> None:
        self.dict[number]+=1
        self.dict2[self.dict[number]-1] -=1
        self.dict2[self.dict[number]]+=1
    def deleteOne(self, number: int) -> None:
        if self.dict[number]:
            self.dict[number]-=1
            if self.dict[number]==0:
                del self.dict[number]
            self.dict2[self.dict[number]]+=1
            self.dict2[self.dict[number]+1]-=1
    def hasFrequency(self, frequency: int) -> bool:
        if self.dict2[frequency]>0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)