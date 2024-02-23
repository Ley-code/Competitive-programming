class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        self.size = k
    def enQueue(self, value: int) -> bool:
        if self.length<self.size:
            newnode = Node(value)
            temp = self.tail.prev
            temp.next = newnode
            newnode.prev = temp
            self.tail.prev = newnode
            newnode.next = self.tail
            self.length+=1
            return True
        return False
    def deQueue(self) -> bool:
        if self.length!=0:
            temp = self.head.next.next
            self.head.next.prev = None
            self.head.next.next = None
            self.head.next = temp
            temp.prev = self.head
            self.length-=1
            return True
        return False

    def Front(self) -> int:
        if self.length!=0:
            return self.head.next.val
        return -1

    def Rear(self) -> int:
        if self.length!=0:
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        if self.length:
            return False
        return True

    def isFull(self) -> bool:
        if self.length == self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()