# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

for _ in range(int(input())):
  n = int(input())
  if n==2:
    print(-1)
  else:
    ans = []
    count = 0
    temp = []
    while count<2:
      
      for i in range(count+1,(n*n)+1,2):
        temp.append(i)
        if len(temp)==n:
          ans.append(temp)
          temp = []

      count+=1
    for row in ans:
      print(*row)
