# Problem: Throne Inheritance - https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.familyTree = {kingName : []}        
        self.dead = set()
        self.king = kingName
    def birth(self, parentName: str, childName: str) -> None:
        self.familyTree[parentName].append(childName)
        self.familyTree[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(name):
            if name not in self.dead:
                order.append(name)
            if not self.familyTree[name]:
                return
            for childName in self.familyTree[name]:
                dfs(childName)
        dfs(self.king)
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()