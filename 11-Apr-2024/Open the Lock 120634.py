# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendset = set(deadends)
        visited = set()
        q = deque([["0000",0]])
        while q:
            curstr,turns = q.popleft()
            if curstr == target:
                return turns
            if curstr in deadendset:
                continue
            for i in range(4):
                digit = int(curstr[i])
                for direction in [1,-1]:
                    newdigit = (digit+direction)%10
                    newstr = curstr[:i]+str(newdigit)+curstr[i+1:]
                    if newstr not in visited:
                        q.append([newstr,turns+1])
                        visited.add(newstr)
        return -1
