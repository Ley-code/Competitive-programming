def conveyorbelts(values):
    n = values[0]
    strt_postion = []
    end_postion = []
    for i in range(1,len(values)):
        if i<=2:
            if values[i]<=n/2:
                strt_postion.append(values[i]-1)
            else:
                strt_postion.append(n-values[i])
        else:
            if values[i]<=n/2:
                end_postion.append(values[i]-1)
            else:
                end_postion.append(n-values[i])
    return abs(min(strt_postion)-min(end_postion))
for i in range(int(input())):
    values = list(map(int,input().split()))
    print(conveyorbelts(values))
    