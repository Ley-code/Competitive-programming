class ATM:

    def __init__(self):
        self.storage = [0]*5
        self.notes = [20,50,100,200,500]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.storage[i] += banknotesCount[i]
    def withdraw(self, amount: int) -> List[int]:
        take = [0]*5
        for i in range(4,-1,-1):
            take[i] = min(self.storage[i],amount//self.notes[i])
            amount -= take[i]*self.notes[i]
        if amount == 0:
            self.storage = [st - tk for st,tk in zip(self.storage,take)]
        return [-1] if amount else take



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)