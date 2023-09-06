ndials = int(input())
values = []
for i in range(ndials):
    value = list(map(int,input().split()))
    values.append((value[1]-value[0]+1))
def totalcombination(values):
    total = 1
    for i in values:
        total*= i
    return total
print(totalcombination(values))
