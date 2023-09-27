def mostcommon(array,integer):
    if integer in array:
        return "YES"
    return "NO"
testcases=int(input())
for i in range(testcases):
    firstline = list(map(int,input().split()))
    array = list(map(int,input().split()))
    print(mostcommon(array,firstline[1]))