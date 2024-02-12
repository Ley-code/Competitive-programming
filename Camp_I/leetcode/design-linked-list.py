class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def get(self, index: int) -> int:
        currnode = self.head
        curridx = 0
        if index<self.size:
            while curridx!=index:
                currnode = currnode.next
                curridx+=1
            return currnode.value
        return -1
    def addAtHead(self, val: int) -> None:
        newhead = Node(val)
        newhead.next = self.head
        self.head = newhead
        self.size+=1
    def addAtTail(self, val: int) -> None:
        currnode = self.head
        if currnode==None:
            self.addAtHead(val)
        else:
            while currnode.next!=None:
                currnode = currnode.next
            lastnode = Node(val)
            currnode.next = lastnode
            self.size+=1
    def addAtIndex(self, index: int, val: int) -> None:
        newnode = Node(val)
        prevnode = Node(None)
        currnode = self.head
        curridx = 0
        if index<=self.size:
            while curridx!=index :
                prevnode = currnode 
                currnode = currnode.next
                curridx+=1
            prevnode.next = newnode
            if index == 0:
                self.head = newnode
            newnode.next = currnode
            self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        prevnode = Node(None)
        currnode = self.head
        curridx = 0
        if index<self.size:
            while curridx!=index:
                prevnode = currnode
                currnode = currnode.next
                curridx+=1
            prevnode.next = currnode.next
            if index == 0:
                self.head = currnode.next
            currnode.next = None
            self.size -=1    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)