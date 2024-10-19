# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robot = defaultdict(list)
        for i in range(len(positions)):
            robot[positions[i]] = [directions[i],healths[i],i]
        positions.sort()

        stack = []
        for pos in positions:
            
            flag = False
            while stack and robot[stack[-1]][0]=="R" and robot[pos][0]=="L":
                prevD,prevH,previdx = robot[stack[-1]][0],robot[stack[-1]][1],robot[stack[-1]][2]
                curD,curH,curidx = robot[pos][0],robot[pos][1],robot[pos][2]
                if prevH==curH:
                    flag = True
                    stack.pop()
                    break
                elif prevH>curH:
                    robot[stack[-1]] = [prevD,prevH-1,previdx]
                    flag = True
                    break
                else:
                    robot[pos] = [curD,curH-1,curidx]
                    stack.pop()
            if flag: continue
            stack.append(pos)

        stack.sort(key= lambda x:robot[x][2])
        for i,pos in enumerate(stack):
            stack[i] = robot[pos][1]
        return stack