class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0] if len(self.queue)!=0 else None

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()