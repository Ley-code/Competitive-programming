import math
numbers = []
for i in range(4):
    numbers.append(int(input()))
print(math.sqrt(pow(numbers[2]-numbers[0],2)+pow(numbers[3]-numbers[1],2)))