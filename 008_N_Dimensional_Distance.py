import math


dimensions = int(input())
values = []
sum = 0
for i in range(dimensions*2):
    values.append(int(input()))
for j in range(0,dimensions*2,2):   
    sum += pow(values[j+1]-values[j],2)
print(math.sqrt(sum))
