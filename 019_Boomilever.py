number = list(map(int,input().split()))
appliedpound = list(map(int,input().split()))
count = 0
for i in range(number[0]):
    if appliedpound[i] >= number[1]:
        count+=1
print(count)

