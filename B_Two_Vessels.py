def twovessels(bottle1,bottle2,cup):
    higher = max(bottle1,bottle2)
    lower = min(bottle1,bottle2)
    count = 0
    while higher>lower:
        higher-=cup
        lower+=cup
        count+=1
    return count
testcase = int(input())
for i in range(testcase):
    values = list(map(int,input().split()))
    print(twovessels(values[0],values[1],values[2]))