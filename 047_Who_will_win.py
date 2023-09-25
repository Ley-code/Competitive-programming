runners = []
for i in range(2):
    runners.append(list(map(str,input().split())))
time1 = (400-float(runners[0][13]))/float(runners[0][5])
time2 = (400-float(runners[1][13]))/float(runners[1][5])
if time2> time1:
    print("Runner 1 wins")
else:
    print("Runner 2 wins")