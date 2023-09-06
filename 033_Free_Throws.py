numberofplayers = int(input())
eachplayer = []
made = []
attempted = []
for i in range(numberofplayers):
    freethrows = list(map(int,input().split()))
    made.append(freethrows[0])
    attempted.append(freethrows[1])
def average(made,attempted):
    return round((sum(made)/sum(attempted))*100,2)

print(average(made,attempted))
