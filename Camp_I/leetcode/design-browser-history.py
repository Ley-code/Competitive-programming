class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        curr = self.curr
        newnode = Node(url)
        curr.next = newnode
        newnode.prev = curr
        self.curr = newnode
    def back(self, steps: int) -> str:
        curr = self.curr
        while steps>0 and curr and curr.prev:
            curr = curr.prev
            steps-=1
        self.curr = curr
        return curr.value
    def forward(self, steps: int) -> str:
        curr = self.curr
        while steps>0 and curr and curr.next:
            curr = curr.next
            steps-=1
        self.curr = curr
        return curr.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)