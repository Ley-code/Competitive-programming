# Problem: E - Blocking Paths for Safe Escape - https://codeforces.com/gym/515998/problem/E



import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def inbound(r,c):
        return 0<=r<n and 0<=c<m
    def dfs(node):
        count = 0
        r,c = node
        visited.add(node)
        if graph[r][c]=="G":
            count+=1
        if graph[r][c]=="#" or graph[r][c] == "B":
            return count
        for dr,dc in directions:
            newr,newc = r+dr,c+dc
            if inbound(newr,newc) and (newr,newc) not in visited:
                count = count + dfs((newr,newc))
        return count
    for i in range(int(input())):
        n,m = map(int,input().split())
        graph = []
        for i in range(n):
            graph.append(list(input()))

        ngood = 0
        flag = True
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(n):
            for j in range(m):
                if graph[i][j]=="B":
                    for dr,dc in directions:
                        newr,newc = i+dr,j+dc
                        if inbound(newr,newc):
                            if graph[newr][newc]==".":
                                graph[newr][newc] = "#"
                            elif graph[newr][newc] == "G":
                                flag= False
                                break
                if graph[i][j]=="G":
                    ngood+=1
        if not flag:
            print("No")
        else:
            visited = set()
            count =dfs((n-1,m-1))
            if count==ngood:
                print("Yes")
            else:
                print("No")
        
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()