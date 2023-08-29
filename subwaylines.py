subwaylines = int(input())
lines = []
for i in range(subwaylines):
    lines.append(list(map(str,input().split()))) 
def search(laststation):
    for firststation in range(subwaylines):
        if lines[firststation][0] == laststation:
            return firststation
def linechecker(firststation,numberoflines):
    laststation = lines[firststation][-1]
    if laststation == "Hotel":
        return numberoflines
    return linechecker (search(laststation),numberoflines+1)
def starter():
    for i in range(subwaylines):
        if lines[i][0] == "Airport":
            return i
linechecker(starter(),1)