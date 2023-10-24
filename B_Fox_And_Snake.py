def oddnumbers(n):
    list = []
    for i in range(1,n+1,2):
        list.append(i)
    return list
    
def foxandsnake(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i in oddnumbers(n):
                print("#",end="")
            if i not in oddnumbers(n) and i%2 == 0 and i%4 != 0 and j==m:
                print("#",end="")
            if i not in oddnumbers(n) and i%4 == 0 and j == 1:
                print("#",end="")
            elif i not in oddnumbers(n) and i%2 == 0 and j!=m:
                print(".",end="")
            elif i not in oddnumbers(n) and i%4 == 0 and j!=1:
                print(".",end="")
        print()
n,m = map(int,input().split())
foxandsnake(n,m)
                
