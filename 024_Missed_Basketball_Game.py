teams = list(map(str,input().split()))
placeholder =[]
score = []
team1 = []
team2 = []
team = [team1,team2]

for i in range(3):
    placeholder.append(list(map(int,input().split())))
for each in placeholder:
    team1.append(each[0])
    team2.append(each[1])
def scorecalculator(numbasket,threepoint,freethrows):
        twopoint = numbasket - threepoint
        return (threepoint*3+twopoint*2+freethrows)
def compare(team1,team2):
    if team1> team2:
         return teams[0]
    else:
         return teams[1]

score.append(scorecalculator(team[0][0],team[0][1],team[0][2]))
score.append(scorecalculator(team[1][0],team[1][1],team[1][2]))
print(compare(score[0],score[1]))