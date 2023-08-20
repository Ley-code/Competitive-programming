n = int(input())
sides = []
sum = 0
for i in range(n):
    sides.append(int(input()))
for i in sides:
    sum += (i*3)
print(sum)