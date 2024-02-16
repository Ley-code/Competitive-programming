class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.size = 0
        self.count = 0
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num==self.value:
            self.count+=1
        self.size+=1
        if self.size<self.k:
            return False
        elif self.size>self.k:
            val = self.queue.popleft()
            if val == self.value:
                self.count-=1
            self.size-=1
        return self.count==self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)