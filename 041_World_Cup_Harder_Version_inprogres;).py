gamesplayed = int(input())
first = []
second = []
points = []
matches = []
finaloutput = {}
def gamechecker(point):
    firstpoint = 0
    secondpoint = 0
    if point == "W":
        firstpoint+=3
    else:
        firstpoint+=1
        secondpoint+=1
    return [firstpoint,secondpoint]
def teams(first,second):
    totalteam = []
    for team in first:
        if totalteam.count(team) == 0:
            totalteam.append(team)
    for team in second:
        if totalteam.count(team) == 0:
            totalteam.append(team)
    return totalteam

for i in range(gamesplayed):
    matches.append(list(map(str,input().split())))
    points.append(matches[i][2])
    first.append(matches[i][0])
    second.append(matches[i][1])
teams = teams(first,second)

for i in range(len(teams)):
    finaloutput[teams[i]] = 0
for i in range(gamesplayed):
    finaloutput[first[i]]= finaloutput.get(first[i]) + gamechecker(points[i])[0]
    finaloutput[second[i]] = gamechecker(points[i])[1] + finaloutput.get(second[i])
for i in range(len(teams)):
    print(teams[i]+" " + str(finaloutput.get(teams[i])))
    



