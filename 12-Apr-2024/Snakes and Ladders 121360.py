# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        path = []
        for r in range(len(board)-1,-1,-1):
            if len(board)%2==0:
                if r%2==0:
                    for j in range(len(board)-1,-1,-1):
                        path.append(board[r][j])
                else:
                    for j in range(len(board)):
                        path.append(board[r][j])
            else:
                if r%2==0:
                    for j in range(len(board)):
                        path.append(board[r][j])
                else:
                    for j in range(len(board)-1,-1,-1):
                        path.append(board[r][j])
        q = deque([0])
        n = len(path)-1
        level = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur>=n:
                    return level
                for i in range(1,7):
                    if cur+i<=n and path[cur+i]!=0:
                        if path[cur+i]==-1:
                            q.append(cur+i)
                        else:
                            q.append(path[cur+i]-1)
                        path[cur+i]=0
            level+=1
        return -1