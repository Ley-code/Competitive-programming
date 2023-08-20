grid = list(map(int,input().split()))
labyrinth = []
for i in range(grid[0]):
    labyrinth.append(input())
trap = 0
for row in labyrinth:
    for letter  in row:
        if letter == "x":
            trap+=1
print(trap) 

