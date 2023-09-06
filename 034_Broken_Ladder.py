ladder = list(map(int,input().split()))
rungs = list(map(int,input().split()))
def checker():
    holder = True
    for i in range(ladder[0]-1):
        if rungs[i+1] - rungs[i] > ladder[1]:
            holder = False
    return holder
def output(checker):
    if checker == False:
        return "NO"
    return "YES"
print(output(checker()))