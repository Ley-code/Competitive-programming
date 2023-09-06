itemsnumber = int(input())
numbers = list(map(int,input().split()))
distinct = len(numbers)
for i in numbers:
    if numbers.count(i) !=1:
        distinct-=(numbers.count(i)-(numbers.count(i)-1))
    pass
new = []
for i in numbers:
    if new.count(i) == 0:
        new.append(i)
print(len(new))