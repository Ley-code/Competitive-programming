class OrderedStream:

    def __init__(self, n: int):
        self.pointer = 0
        self.list = [None]*(n)

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -=1
        self.list[idKey] = value
        if idKey > self.pointer:
            return []
        while self.pointer<len(self.list) and self.list[self.pointer]:
            self.pointer+=1
        return self.list[idKey:self.pointer]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)