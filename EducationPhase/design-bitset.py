class Bitset:

    def __init__(self, size: int):
        self.bitset = ["0"]*size
        self.bitsetopp = ["1"]*size
        self.counter = 0
        self.size = size
    def fix(self, idx: int) -> None:
        if self.bitset[idx] == "0":
            self.bitset[idx] = "1"
            self.counter+=1
            self.bitsetopp[idx] = "0"
            
    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == "1":
            self.bitset[idx] = "0"
            self.counter -=1
            self.bitsetopp[idx] = "1"
            
    def flip(self) -> None:
        temp = self.bitset
        self.bitset = self.bitsetopp
        self.bitsetopp = temp
        self.counter = self.size - self.counter
    def all(self) -> bool:
        if self.counter == self.size:
            return True
        return False
    def one(self) -> bool:
        if self.counter > 0:
            return True
        return False
    def count(self) -> int:
        return self.counter
    def toString(self) -> str:
        return "".join(self.bitset)
# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()